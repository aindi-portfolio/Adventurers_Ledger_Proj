from django.urls import path
from .views_EXPERIMENTAL import SeedItemsView, GetRandomItem

urlpatterns = [
    path("seed", SeedItemsView.as_view(), name="seed"),
    path("random", GetRandomItem.as_view(), name="random"),
]
