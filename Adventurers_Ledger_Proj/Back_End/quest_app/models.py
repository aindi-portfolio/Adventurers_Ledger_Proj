from django.db import models

class Quest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ])
    reward_item = models.CharField(max_length=100)
    reward_experience = models.IntegerField()


class Journal(models.Model):
    player = models.OneToOneField('player_app.Player', on_delete=models.CASCADE, related_name='journal')
    entries = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Journal of {self.player.username}"
    

class PlayerQuest(models.Model):
    player = models.OneToOneField('player_app.Player', on_delete=models.CASCADE, related_name='player_quests')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='player_quests')
    status = models.CharField(max_length=50, choices=[
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ])
    started_timestamp = models.DateTimeField(auto_now_add=True)
    completed_timestamp = models.DateTimeField(null=True, blank=True, default=None)




