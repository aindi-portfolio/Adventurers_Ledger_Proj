from rest_framework.serializers import ModelSerializer
from .models import Quest

class QuestSerializer(ModelSerializer):
    """
    Serializer for Quest model.
    """
    class Meta:
        model = Quest
        fields = '__all__'