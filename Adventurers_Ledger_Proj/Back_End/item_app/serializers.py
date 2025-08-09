from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Item, ShopItem

class ItemSerializer(ModelSerializer):
    """
    Serializer for Item model.
    """
    class Meta:
        model = Item
        fields = '__all__'
    
class ShopItemSerializer(ModelSerializer):
    """
    Serializer for ShopItem model.
    """
    item = ItemSerializer(read_only=True)

    class Meta:
        model = ShopItem
        fields = '__all__'

    # def validate(self, data):
    #     if data['stock'] < 0:
    #         raise serializers.ValidationError("Stock cannot be negative.")
    #     if data['price'] < 0:
    #         raise serializers.ValidationError("Price cannot be negative.")
    #     return data