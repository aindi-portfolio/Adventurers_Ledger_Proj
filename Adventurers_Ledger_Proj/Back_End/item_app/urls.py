from django.urls import path
from .views_EXPERIMENTAL import SeedItemsView, GetRandomItem, AddItemToShopView, GetItemByNameView

urlpatterns = [
    path("seed", SeedItemsView.as_view(), name="seed"), # 'api/items/'
    path("item-by-name", GetItemByNameView.as_view(), name="item_by_name"),
    path("random", GetRandomItem.as_view(), name="random"),
    path("add-to-shop", AddItemToShopView.as_view(), name="add_to_shop"),
]
