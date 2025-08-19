from django.urls import path
from .views import InventoryManager, ManageCharacter, CharacterStats

urlpatterns = [
    path('inventory', InventoryManager.as_view(), name='inventory'),
    path('manage-character', ManageCharacter.as_view(), name='manage_character'),
    path('stats', CharacterStats.as_view(), name='stats'),
]