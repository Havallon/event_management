from rest_framework import serializers
from event import models


class EventSerializer(serializers.ModelSerializer):
    producer = serializers.UUIDField(source='producer.id', required=False)

    class Meta:
        model = models.Event
        fields = ['id', 'banner', 'producer']


class SectionSerializer(serializers.ModelSerializer):
    event = serializers.UUIDField(source='event.id', required=False)

    class Meta:
        model = models.Section
        fields = ['id', 'section_type', 'event']
