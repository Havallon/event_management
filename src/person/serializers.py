from rest_framework import serializers
from person.models import Person
from person.choices import PersonRole


class CreatePersonSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=255)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, max_length=128)
    document = serializers.CharField(required=True, max_length=255)
    phone_number = serializers.CharField(required=True, max_length=255)
    role = serializers.IntegerField(required=True)

    def validate_email(self, value):
        if Person.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email has been used')
        return value
    
    def validate_document(self, value):
        if Person.objects.filter(document=value).exists():
            raise serializers.ValidationError('This document has been used')
        return value

    def validate_role(self, value):
        if value not in PersonRole:
            raise serializers.ValidationError('Out of range')
        if value == PersonRole.admin:
            raise serializers.ValidationError('not allowed')
        return value


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'email', 'document', 'phone_number', 'role', 'is_active', 'created_at']
