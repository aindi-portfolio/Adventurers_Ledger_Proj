from django.db import models

# Create your models here.
class Monster(models.Model):
    """
    This model represents a monster in the game.
    """
    name = models.CharField(max_length=100, unique=True)
    base_health = models.IntegerField(default=100)
    base_damage = models.IntegerField(default=10)
    element_type = models.CharField(
        max_length=50,
        choices=[
            ('fire', 'Fire'),
            ('water', 'Water'),
            ('normal', 'Normal'),
            ('air', 'Air'),
            ],
        default='normal')
    image_url = models.URLField(max_length=200, blank=True, null=True)