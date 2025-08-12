from django.urls import path
from .views import InventoryManager, CreateCharacter, CharacterStats

urlpatterns = [
    path('inventory', InventoryManager.as_view(), name='inventory'),
    path('create-character', CreateCharacter.as_view(), name='create_character'),
    path('stats', CharacterStats.as_view(), name='stats'),
]