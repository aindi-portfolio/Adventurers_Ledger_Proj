from django.db import models

# Create your models here.
class Item(models.Model):
    """
    This model represents an item in the game.
    """
    ITEM_TYPES = [
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('potion', 'Potion'),
        ('misc', 'Miscellaneous'),
    ]

    name = models.CharField(max_length=100, unique=True, default='Unknown Item')
    item_type = models.CharField(max_length=50, choices=ITEM_TYPES, default='misc')

    damage = models.IntegerField(default=0)  # Damage value for weapons
    armor_class = models.IntegerField(default=0)  # Armor class for armor
    healing = models.IntegerField(default=0)  # Healing value for potions

    effect = models.CharField(max_length=100, blank=True, null=True, default='No special effect.')
    description = models.TextField(blank=True, null=True, default='No description available.')

    rarity = models.CharField(max_length=50, blank=True, null=True, default='common')
    source = models.CharField(max_length=50, default='api', blank=True, null=True)

    is_starter = models.BooleanField(default=False)  # Indicates if this is a starter item

    def __str__(self):
        return self.name
    


    
class ShopItem(models.Model):
    """
    This model represents an item available in the shop.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='shop_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} - {self.price} gold"