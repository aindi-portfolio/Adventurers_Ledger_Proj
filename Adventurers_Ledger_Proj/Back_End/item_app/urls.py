from django.urls import path
from .views import SeedWeaponsView

urlpatterns = [
    path("seed-weapons", SeedWeaponsView.as_view(), name="seed-weapons"),
]
