from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as s
from rest_framework.response import Response
from .serializers import InventorySerializer, Inventory, Character, CharacterSerializer
from item_app.views import ItemSerializer
from user_app.models import UserAccount
from item_app.models import Item
import requests
from item_app.utils import get_dice_average
import traceback
from .utils.levelingLogic import applyExperienceGain

# Create your views here.
class ManageCharacter(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request): # Make a new character, give it starting items based on class selection

        STARTER_ITEMS_FOR_CLASSES = [ # For future class selection, these are the starter item by name (not index in D&D API)
                {
                    "class": "barbarian",
                    "items":
                        {
                            "Handaxe": 2,
                            "Chain Mail": 1
                        } # Future enhancement: let user select class and starting weapon
                },
                {
                    "class": "fighter",
                    "items":
                        {
                            "Longsword": 1,
                            "Shield": 1,
                            "Chain Mail": 1
                        }
                },
                {
                    "class": "wizard",
                    "items":
                        {
                            "Quarterstaff": 1,
                            "Spellbook": 1,
                            "Component Pouch": 1
                        } # Build is in progress, will be added later
                },
                {
                    "class": "rogue",
                    "items":
                        {
                            "Shortsword": 1,
                            "Dagger": 1,
                            "Leather Armor": 1
                        }
                }
            ]
        
        try:
            user_account = request.user
            # Check if the user_account already has a character with the same character_class and name
            if Character.objects.filter(
                user_account=user_account,
                name=request.data.get('name'),
                character_class=request.data.get('character_class')
            ).exists():
                return Response(
                    {"message": "Character with this name and class already exists."},
                    status=s.HTTP_400_BAD_REQUEST
                )



            name = request.data.get('name')
            character_class = request.data.get('character_class')

            if not name or not character_class:
                return Response({"message": "Missing required fields."}, status=s.HTTP_400_BAD_REQUEST)

            # Step 1: Create the character
            character = Character.objects.create(
                user_account=user_account,
                name=name,
                character_class=character_class
            )
            character.save()

            # Step 2: Fetch item data from the D&D API based on the character class and starter items
            class_entry_match = next((item for item in STARTER_ITEMS_FOR_CLASSES if item['class'] == character_class.lower()), None)
            
            if class_entry_match:
                for item_name, quantity in class_entry_match['items'].items(): # item_name is the name of the item, quantity is how many to add to the inventory
                    item_name_slug = item_name.lower().replace(' ', '-') # Convert item name to slug format for API URL
                    item_obj = Item.objects.filter(name=item_name).first()

                    if not item_obj: # If the item does not exist in the database, fetch it from the D&D API
                        item = requests.get(f"https://www.dnd5eapi.co/api/equipment/{item_name_slug}")

                        item_data = item.json()
                        damage_dice = item_data.get('damage', {}).get('damage_dice')
                        item_obj, _ = Item.objects.get_or_create(
                            name=item_data['name'],
                            defaults = {
                                'item_category': item_data.get('equipment_category', {}).get('name', 'Unknown'),
                                'damage': get_dice_average(damage_dice) if damage_dice else 0,
                                'armor_class': item_data.get('armor_class', {}).get('base', 0),
                                'healing': 0,
                                'rarity': item_data.get('rarity', {}).get('name', 'common'),
                                'description': item_data.get('desc', 'No description available.'),
                                'cost_amount': item_data.get('cost', {}).get('quantity', 0),
                                'cost_unit': item_data.get('cost', {}).get('unit', 'gp'),
                                'is_starter': True
                            }
                        )
                        item_obj.save() # Save it to the database

                        if item.status_code != 200:
                            return Response({"message": f"Failed to fetch starter item data for {item_name}."}, status=s.HTTP_502_BAD_GATEWAY)

                    # Step 3: Add the item and its quantity to the character's inventory
                    Inventory.objects.create(character=character, item=item_obj, quantity=quantity)

            # Step 4: Serialize the character and return the response
            serialized_character = CharacterSerializer(character)
            return Response(serialized_character.data, status=s.HTTP_201_CREATED)

        except Exception as e:
            print("Exception during character creation:", e)
            traceback.print_exc()
            return Response({"message": str(e)}, status=s.HTTP_500_INTERNAL_SERVER_ERROR)


    ## Update the cahracter attributes (like level, experience, health, gold)
    def put(self, request):
        try:
            user_account = request.user
            working_character = Character.objects.get(user_account=user_account)
            # print(working_character.__repr__())
            working_character.health = request.data.get('health')
            # print(f"Updated Health: {working_character.health}")
            working_character.gold = request.data.get('gold')
            # print(f"Updated Gold: {working_character.gold}")
            
            # Update level and experience
            # working_character.level = request.data.get('level')
            # working_character.experience = request.data.get('experience')
            working_character = applyExperienceGain(working_character, request.data.get('experience'))
            # print(f"-----result from the LEVELING LOGIC: {working_character.__repr__()}")

            working_character.save()
            serialized_character = CharacterSerializer(working_character)
            return Response(serialized_character.data, status=s.HTTP_202_ACCEPTED)
        except Exception as e:
            traceback.print_exc()
            print(f"Error: {e}")
            return Response(f"Error updating character: {e}", status=s.HTTP_400_BAD_REQUEST)
        


    def delete(self,request):
        try:
            user_account = request.user
            working_character = Character.objects.get(user_account=user_account)
            working_character.dele
            working_character
        except Exception as e:
            traceback.print_exc()
            print(f"Error: {e}")
            return Response(f"Error deleting character: {e}", status=s.HTTP_400_BAD_REQUEST)

class CharacterStats(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_account = request.user
        try:
            character = Character.objects.get(user_account=user_account)
            serialized_character = CharacterSerializer(character)
            return Response(serialized_character.data, status=s.HTTP_200_OK)
        except Character.DoesNotExist:
            return Response({"message": "Character not found."}, status=s.HTTP_404_NOT_FOUND)


class InventoryManager(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # print(request.user)
            character = Character.objects.get(user_account=request.user)
            inventory = Inventory.objects.filter(character=character)
            serialized_inventory = InventorySerializer(inventory, many=True)
            # print(serialized_inventory.data)
            return Response(serialized_inventory.data,status=s.HTTP_200_OK)
        except Character.DoesNotExist:
            return Response({"message": "Character not found."}, status=s.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"message": "Inventory not found."}, status=s.HTTP_404_NOT_FOUND)
    