from django.urls import path
from .views import SeedMonstersView, RandomMonsterByCR

urlpatterns = [
    path("seed-monsters", SeedMonstersView.as_view(), name="seed-monsters-by-level"), # preceded by /api/monsters/
    path("<int:level>", RandomMonsterByCR.as_view(), name="fetch-by-character-level"),
]
