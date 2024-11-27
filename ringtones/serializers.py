from rest_framework import serializers
from .models import Ringtone

class RingtoneSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField(read_only=True)  # Remove the `source` argument

    class Meta:
        model = Ringtone
        fields = ['id', 'user', 'name', 'file', 'description', 'genre', 'tags', 'total_likes', 'date_uploaded']
