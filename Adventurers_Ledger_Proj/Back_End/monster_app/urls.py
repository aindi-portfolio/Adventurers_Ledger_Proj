from django.urls import path
from .views import SeedMonstersView, RandomMonsterByCR

urlpatterns = [
    path("seed-monsters", SeedMonstersView.as_view(), name="seed-monsters"), # preceded by /api/monsters/
    path("<int:challenge_rating>", RandomMonsterByCR.as_view(), name="fetch-by-cr"),
]
