from rest_framework import serializers
from .models import Ringtone

class RingtoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ringtone
        fields = ['id', 'user', 'name', 'file', 'description', 'genre', 'tags', 'likes', 'date_uploaded']
