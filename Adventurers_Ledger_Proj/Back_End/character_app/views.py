from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as s
from rest_framework.response import Response
from .serializers import InventorySerializer, Inventory, Character, CharacterSerializer
from item_app.models import Item

# Create your views here.
class CreateCharacter(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_account = request.user
            if Character.objects.filter(user_account=user_account).exists():
                return Response({"message": "Character already exists for this user."}, status=s.HTTP_400_BAD_REQUEST)

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

            # Step 2: Get starter items
            starter_items = Item.objects.filter(is_starter=True)

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
    