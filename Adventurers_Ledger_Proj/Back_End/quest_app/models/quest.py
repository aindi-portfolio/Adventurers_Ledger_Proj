from django.db import models

# Create your models here.
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