from django.urls import path
from .views import InventoryManager, CreatePlayer

urlpatterns = [
    path('inventory', InventoryManager.as_view(), name='inventory'),
    path('create', CreatePlayer.as_view(), name='create_player'),
]