# user_app/signals.py
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from user_app.models import UserAccount
# from player_app.models import Player

# @receiver(post_save, sender=UserAccount)
# def create_player_for_user(sender, instance, created, **kwargs):
#     if created:
#         Player.objects.create(user_account=instance)
