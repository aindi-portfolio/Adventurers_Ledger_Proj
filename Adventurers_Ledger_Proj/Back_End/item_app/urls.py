from django.urls import path
from .views_EXPERIMENTAL import SeedItemsView

urlpatterns = [
    path("seed", SeedItemsView.as_view(), name="seed"),
]
