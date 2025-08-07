from django.db import models

class ShopItem(models.Model):
    """
    This model represents an item available in the shop.
    """
    item = models.ForeignKey('item_app.Item', on_delete=models.CASCADE, related_name='shop_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.name} - {self.price} gold"