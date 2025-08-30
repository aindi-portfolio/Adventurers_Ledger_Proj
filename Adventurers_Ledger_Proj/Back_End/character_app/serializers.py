from .models import Character, Inventory, Transaction
from user_app.serializers import UserAccountSerializer
from item_app.serializers import ItemSerializer
from django.core.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

class CharacterSerializer(ModelSerializer):
    # user_account = UserAccountSerializer(read_only=True)
    class Meta:
        model = Character
        fields = ["name", "character_class", "level", "experience", "health", "gold"]

    # def validate(self, data):
    #     if data['level'] < 1:
    #         raise ValidationError("Level must be at least 1.")
    #     if data['health'] < 0:
    #         raise ValidationError("Health cannot be negative.")
    #     return data

class InventorySerializer(ModelSerializer):
    character = CharacterSerializer(read_only=True)
    item = ItemSerializer(read_only=True)
    class Meta:
        model = Inventory
        fields = '__all__'

    # def validate(self, data):
    #     if data['quantity'] < 1:
    #         raise ValidationError("Quantity must be at least 1.")
    #     return data

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    # def validate(self, data):
    #     if data['quantity'] < 1:
    #         raise ValidationError("Quantity must be at least 1.")
    #     if data['total_price'] < 0:
    #         raise ValidationError("Total price cannot be negative.")
    #     return data