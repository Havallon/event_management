from rest_framework import exceptions
from rest_framework.request import Request
from event import models, serializers
from person.choices import PersonRole


def __get_one(request, id) -> models.Event:
    try:
        queryset = models.Event.objects.get(id=id)
        if request.user.role == PersonRole.admin or queryset.producer == request.user:
            return queryset
        raise exceptions.PermissionDenied("This event isn't yours")
    except models.Event.DoesNotExist:
        raise exceptions.NotFound('Event not found')


def get_all(request: Request) -> list:
    user = request.user
    queryset = models.Event.objects.filter(producer=user)
    serializer = serializers.EventSerializer(queryset, many=True)
    return serializer.data


def create_event(request: Request) -> dict:
    user = request.user
    data = request.data
    data['producer'] = user.id
    validate_serializer = serializers.EventSerializer(data=data)
    validate_serializer.is_valid(raise_exception=True)
    validate_serializer.save()
    return validate_serializer.data


def get_by_id(request: Request, id):
    event = __get_one(request, id)
    serializer = serializers.EventSerializer(event)
    return serializer.data


def update(request, id):
    instance = __get_one(request, id)
    request.data.pop('producer', None)
    validade_serializer = serializers.EventSerializer(instance=instance, data=request.data)
    validade_serializer.is_valid(raise_exception=True)
    validade_serializer.save()
    return validade_serializer.data


def destroy(request, id):
    instance = __get_one(request, id)
    instance.delete()
    return
