from django.db import models

# Create your models here.
class Player(models.Model):
    """
    Player gets created when a user signs up.
    """
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    health = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)