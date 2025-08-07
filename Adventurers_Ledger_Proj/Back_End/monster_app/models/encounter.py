from django.db import models

# Create your models here.
class Encounter(models.Model):
    """
    This model represents an encounter in the game.
    """
    player = models.ForeignKey('player_app.Player', on_delete=models.CASCADE, related_name='encounters')
    monster = models.ForeignKey('monster_app.Monster', on_delete=models.CASCADE, related_name='encounters')
    monster_level = models.IntegerField(default=1)
    outcome = models.CharField(max_length=50, choices=[
        ('victory', 'Victory'),
        ('defeat', 'Defeat'),
        ('flee', 'Flee')
    ], default='defeat')
    timestamp = models.DateTimeField(auto_now_add=True)