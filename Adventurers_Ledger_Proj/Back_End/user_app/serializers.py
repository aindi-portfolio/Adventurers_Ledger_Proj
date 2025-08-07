from .models import UserAccount
from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"

    def create(self, validated_data):
        new_user_account = UserAccount.objects.create_user(**validated_data)
        new_user_account.save()
        return new_user_account