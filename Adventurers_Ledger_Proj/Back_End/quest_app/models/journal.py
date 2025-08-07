from django.db import models

# Create your models here.
class Journal(models.Model):
    player = models.OneToOneField('player_app.Player', on_delete=models.CASCADE, related_name='journal')
    entries = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Journal of {self.player.username}"