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

# Create your views here.
class CreateCharacter(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    STARTER_ITEMS_FOR_CLASSES = [ # For future class selection, these are the starter item by name (not index in D&D API)
            {
                "class": "barbarian",
                "items": ["Handaxe", "Handaxe", "Chain Mail"] # Future enhancement: let user select class and starting weapon
            },
            {
                "class": "fighter",
                "items": ["Longsword", "Shield", "Chain Mail"]
            },
            {
                "class": "wizard",
                "items": ["Quarterstaff", "Spellbook", "Component Pouch"] # Build is in progress, will be added later
            },
            {
                "class": "rogue",
                "items": ["Shortsword", "Dagger", "Leather Armor"]
            }
        ]

    def post(self, request):
        try:
            user_account = request.user
            # Check if the user_account already has a character with the same character_class
            if UserAccount.objects.filter(name=request.data.get('name')).exists() and UserAccount.objects.filter(character_class=request.data.get('character_class')).exists():
                return Response({"message": "Character class with this name already exists. Change name or pick a different class."}, status=s.HTTP_400_BAD_REQUEST)


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

            # Step 2: Fetch item data from the D&D API based on the character class and starter items
            starter_items = []
            for starter in self.STARTER_ITEMS_FOR_CLASSES:
                if starter["class"] == character_class.lower():
                    starter_items = starter["items"]
                    break
            
            for item_name in starter_items:
                if Item.objects.filter(name=item_name).exists():
                    # If the item already exists, skip fetching it again
                    item_obj, _ = Item.objects.get_or_create(name=item_name)
                    
                    continue
                item = requests.get(f"https://www.dnd5eapi.co/api/equipment/{item_name.lower().replace(' ', '-')}")
                if item.status_code == 200:
                    item_data = item.json()
                    # Create Item object if it doesn't exist
                    item_obj, created = Item.objects.get_or_create(
                        name=item_data['name'],
                        defaults={
                            'item_category': item_data['equipment_category']['name'],
                            'damage': get_dice_average(item_data['damage']['damage_dice']) if 'damage' in item_data else 0,
                            'armor_class': item_data['armor_class']['base'] if 'armor_class' in item_data else 0,
                            'healing': 0,
                            'rarity': item_data['rarity']['name'] if 'rarity' in item_data else 'common',
                            'description': item_data.get('desc', 'No description available.'),
                            'cost_amount': item_data['cost']['quantity'],
                            'cost_unit': item_data['cost']['unit'],
                            'is_starter': True
                        }
                    )
                    item_obj.save()
                else:
                    return Response({"message": f"During Character Creation, failed to fetch starter_item data for {item_name}."}, status=s.HTTP_502_BAD_GATEWAY)
                    
                
            # Step 3: Add starter items to the character's inventory
            for item in starter_items:
                Inventory.objects.create(character=character, item=item, quantity=1)

            # Step 4: Serialize the character and return the response
            serialized_character = CharacterSerializer(character)
            return Response(serialized_character.data, status=s.HTTP_201_CREATED)

        except Exception as e:
            return Response({"message": str(e)}, status=s.HTTP_500_INTERNAL_SERVER_ERROR)
            
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
            print(request.user)
            character = Character.objects.get(user_account=request.user)
            inventory = Inventory.objects.filter(character=character)
            serialized_inventory = InventorySerializer(inventory, many=True)
            print(serialized_inventory.data)
            return Response(serialized_inventory.data,status=s.HTTP_200_OK)
        except Character.DoesNotExist:
            return Response({"message": "Character not found."}, status=s.HTTP_404_NOT_FOUND)
        except Inventory.DoesNotExist:
            return Response({"message": "Inventory not found."}, status=s.HTTP_404_NOT_FOUND)
    