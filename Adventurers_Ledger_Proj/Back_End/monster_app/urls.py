from django.urls import path
from .views import SeedMonstersView

urlpatterns = [
    path("seed-monsters", SeedMonstersView.as_view(), name="seed-monsters"), # preceded by /api/monsters/
]
