from django.urls import path
from .views import SeedWeaponsView, SeedArmorView

urlpatterns = [
    path("seed-weapons", SeedWeaponsView.as_view(), name="seed-weapons"),
    path("seed-armor", SeedArmorView.as_view(), name="seed-armor"),
]
