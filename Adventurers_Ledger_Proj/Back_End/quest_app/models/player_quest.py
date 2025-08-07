from django.db import models

# Create your models here.
class PlayerQuest(models.Model):
    player = models.OneToOneField('player_app.Player', on_delete=models.CASCADE, related_name='player_quests')
    quest = models.ForeignKey('quest_app.Quest', on_delete=models.CASCADE, related_name='player_quests')
    status = models.CharField(max_length=50, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ])
    started_timestamp = models.DateTimeField(auto_now_add=True)
    completed_timestamp = models.DateTimeField(null=True, blank=True, default=None)