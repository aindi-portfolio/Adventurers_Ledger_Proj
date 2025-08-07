from django.db import models

# Create your models here.
class Item(models.Model):
    """
    This model represents an item in the game.
    """
    name = models.CharField(max_length=100, unique=True)
    item_type = models.CharField(max_length=50, choices=[
        ('weapon', 'Weapon'),
        ('armor', 'Armor'),
        ('potion', 'Potion'),
        ('misc', 'Miscellaneous')
    ], default='misc')
    effect = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name