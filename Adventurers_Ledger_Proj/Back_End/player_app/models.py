from django.db import models

class Player(models.Model):
    """
    Player gets created when a user signs up.
    """
    user = models.OneToOneField(
        "user_app.UserAccount", 
        on_delete=models.CASCADE, 
        related_name='player', default=None
    )
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    health = models.IntegerField(default=100)
    gold = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

class Inventory(models.Model):
    """
    Inventory holds items for a player.
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='inventory')
    item_name = models.ForeignKey('item_app.Item', on_delete=models.CASCADE, related_name='inventory_items')
    quantity = models.IntegerField(default=1)


class Transaction(models.Model):
    """
    Transaction records the details of an item purchase.
    """
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=50, choices=[('purchase', 'Purchase'), ('sale', 'Sale')], default='purchase') # Will need addtional integration
    item = models.ForeignKey('item_app.Item', on_delete=models.CASCADE, related_name='transactions')
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)