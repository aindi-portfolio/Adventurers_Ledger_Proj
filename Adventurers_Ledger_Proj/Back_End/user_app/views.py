from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as s
from .serializers import UserAccountSerializer, UserAccount



# Create your views here.
class Sign_Up(APIView):
    def post(self, request):
        data = request.data.copy() # {email, password}
        data["username"] = data["email"]
        new_user_account = UserAccountSerializer(data=data)
        if new_user_account.is_valid():
            new_user_account.save()
            token_object = Token.objects.create(user=new_user_account)
            return Response({"client": new_user_account.username, "token": token_object.key}, status=s.HTTP_201_CREATED)
        else:
            return Response(new_user_account.errors, status=s.HTTP_400_BAD_REQUEST)
        
class Login(APIView):
    def post(self, request):
        data = request.data.copy()  # {email, password}
        user_account = authenticate(
            username=data.get("email"), password=data.get("password")
            )
        if user_account:
            token, _ = Token.objects.get_or_create(user=user_account)
            login(request=request, user=user_account)
            return Response({"user_account": user_account.username, "token": token.key}, status=s.HTTP_200_OK)
        else:
            return Response({"error": "No user matching these credentials"}, status=s.HTTP_404_NOT_FOUND)
        
class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            logout(request)
            return Response(status=s.HTTP_204_NO_CONTENT)
        except Token.DoesNotExist:
            return Response({"error": "Token not found"}, status=s.HTTP_400_BAD_REQUEST)
        
class User_Profile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            user_account = UserAccount.objects.get(username=request.user.email)
            return Response({"email": user_account.email}, status=s.HTTP_200_OK)
        except UserAccount.DoesNotExist:
            return Response({"error": "User not found"}, status=s.HTTP_404_NOT_FOUND)