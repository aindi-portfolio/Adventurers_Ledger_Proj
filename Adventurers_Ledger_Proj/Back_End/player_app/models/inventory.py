from django.db import models

class Inventory(models.Model):
    """
    Inventory holds items for a player.
    """
    player = models.ForeignKey('player_app.Player', on_delete=models.CASCADE, related_name='inventory')
    item_name = models.ForeignKey('item_app.Item', on_delete=models.CASCADE, related_name='inventory_items')
    quantity = models.IntegerField(default=1)