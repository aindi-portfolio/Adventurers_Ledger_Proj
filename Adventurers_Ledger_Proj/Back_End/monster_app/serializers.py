from rest_framework.serializers import ModelSerializer
from .models import Monster

class MonsterSerializer(ModelSerializer):
    class Meta:
        model = Monster
        fields = '__all__'