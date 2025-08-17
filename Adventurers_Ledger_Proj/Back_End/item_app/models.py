from django.db import models

# Create your models here.
class Item(models.Model):
    """
    This model represents an item in the game.
    
    ITEM_CATEGORIES = [## Refered to as equipment_category in D&D API
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('misc', 'Miscellaneous'),
        ('potion', 'Potion'),
        ('tool', 'Tool'), # index 'tools' in D&D API
        ('adventuring_gear', 'Adventuring Gear'),
    ]

    CURRENCY_CHOICES = [
        ('cp', 'Copper Pieces'),
        ('sp', 'Silver Pieces'),
        ('ep', 'Electrum Pieces'),
        ('gp', 'Gold Pieces'),
        ('pp', 'Platinum Pieces'),
    ]
    """
    

    name = models.CharField(max_length=100, unique=True, default='Unknown Item') # Will be taken from name from D&D API
    item_category = models.CharField(max_length=50, default='misc') # from equipment_category.name in D&D API

    damage = models.IntegerField(default=0)  # from damage.damage_dice in D&D API
    armor_class = models.IntegerField(default=0)  # Armor class for armor
    healing = models.IntegerField(default=0)  # Healing value for potions
    rarity = models.CharField(max_length=50, blank=True, null=True, default='common')
    description = models.TextField(blank=True, null=True, default='No description available.')

    cost_amount = models.IntegerField(default=0)  # Cost in gold pieces
    cost_unit = models.CharField(max_length=2, default='gp') # Currency unit, e.g., 'gp' for gold pieces
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