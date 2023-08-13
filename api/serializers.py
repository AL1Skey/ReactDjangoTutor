from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'can_pause', 'skip_vote','create_at')