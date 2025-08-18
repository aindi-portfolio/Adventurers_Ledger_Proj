from django.db import models

# Create your models here.
class Encounter(models.Model):
    """
    This model represents an encounter in the game.
    """
    player = models.ForeignKey('character_app.Character', on_delete=models.CASCADE, related_name='encounters')
    monster = models.ForeignKey('monster_app.Monster', on_delete=models.CASCADE, related_name='encounters')
    monster_level = models.IntegerField(default=10)
    outcome = models.CharField(max_length=50, choices=[
        ('victory', 'Victory'),
        ('defeat', 'Defeat'),
        ('flee', 'Flee')
    ], default='defeat')
    timestamp = models.DateTimeField(auto_now_add=True)


class Monster(models.Model):
    """
    This model represents a monster in the game.
    """
    name = models.CharField(max_length=100, unique=True) # Will be taken from name from D&D API
    type = models.CharField(max_length=50, default="unknown") # Will be categorized from the D&D API
    health = models.IntegerField(default=100)
    damage = models.IntegerField(default=10) # Will be calculated from hit_dice from D&D API
    armor = models.IntegerField(default=10) # Will be taken from armor_class.value from D&D API
    xp = models.IntegerField(default=5) # Will be taken from xp from D&D API
    passive_perception = models.IntegerField(default=5) # Will be taken from senses.passive_perception from D&D API
    challenge_rating = models.FloatField(default=0) # Will be taken from challenge_rating from D&D API
    image_url = models.CharField(max_length=200, blank=True, null=True)