from rest_framework import serializers
from event import models


class EventSerializer(serializers.ModelSerializer):
    producer = serializers.UUIDField(source='producer.id', required=False)

    class Meta:
        model = models.Event
        fields = ['id', 'banner', 'producer']
