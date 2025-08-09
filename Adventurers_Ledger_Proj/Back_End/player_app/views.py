from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as s
from rest_framework.response import Response
from .serializers import InventorySerializer, Inventory, Player, PlayerSerializer

# Create your views here.
class CreatePlayer(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        player = getattr(request.user, 'name', None)
        if player:
            return Response({"message": "Player already exists."}, status=s.HTTP_400_BAD_REQUEST)
        else:
            player = Player.objects.create(user_account=request.user)
            serialized_player = PlayerSerializer(player)
            return Response(serialized_player.data, status=s.HTTP_201_CREATED)


class InventoryManager(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        print(request.user.player)
        inventory = Inventory.objects.get(player=request.user.player)
        serialized_inventory = InventorySerializer(inventory)
        return Response(serialized_inventory.data,status=s.HTTP_200_OK)