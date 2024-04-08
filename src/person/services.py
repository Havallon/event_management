from rest_framework.request import Request
from rest_framework import exceptions
from person.models import Person
from person.serializers import (
    PersonSerializer,
    CreatePersonSerializer,
    PersonUpdateSerializer
)


def __get_one(id) -> Person:
    try:
        queryset = Person.objects.get(id=id)
        return queryset
    except Person.DoesNotExist:
        raise exceptions.NotFound('User not found')


def get_all() -> list:
    queryset = Person.objects.all()
    serializer = PersonSerializer(queryset, many=True)
    return serializer.data


def get_by_id(id) -> dict:
    person = __get_one(id)
    serializer = PersonSerializer(person)
    return serializer.data


def create_person(request: Request) -> dict:
    validate_serializer = CreatePersonSerializer(data=request.data)
    validate_serializer.is_valid(raise_exception=True)
    person = Person.objects.create_user(**validate_serializer.validated_data)
    serializer = PersonSerializer(person)
    return serializer.data


def update(request, id, *args, **kwargs):
    instance = __get_one(id)
    partial = kwargs.pop('partial', False)
    validate_serializer = PersonUpdateSerializer(instance=instance, data=request.data, partial=partial)
    validate_serializer.is_valid(raise_exception=True)
    validate_serializer.save()
    return validate_serializer.data


def partial_update(request, id):
    return update(request, id, partial='partial')


def destroy(id):
    instance = __get_one(id)
    instance.delete()
    return
