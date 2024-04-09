from rest_framework import exceptions
from rest_framework.request import Request
from event import models, serializers
from person.models import PersonRole


def __get_one(id) -> models.Event:
    try:
        queryset = models.Event.objects.get(id=id)
        return queryset
    except models.Event.DoesNotExist:
        raise exceptions.NotFound('Event not found')


def __has_permission(request, event):
    if request.user.role == PersonRole.customer:
        raise exceptions.PermissionDenied('You do not have permission to perform this action')
    if event.producer == request.user:
        return
    raise exceptions.PermissionDenied("This event isn't yours")


def get_all() -> list:
    queryset = models.Event.objects.all()
    serializer = serializers.EventSerializer(queryset, many=True)
    return serializer.data


def create_event(request: Request) -> dict:
    user = request.user
    if user.role == PersonRole.customer:
        raise exceptions.PermissionDenied('You do not have permission to perform this action.')
    data = request.data
    data['producer'] = user.id
    validate_serializer = serializers.EventSerializer(data=data)
    validate_serializer.is_valid(raise_exception=True)
    validate_serializer.save()
    return validate_serializer.data


def get_by_id(id):
    event = __get_one(id)
    serializer = serializers.EventSerializer(event)
    return serializer.data


def update(request, id):
    instance = __get_one(id)
    __has_permission(request, instance)
    request.data.pop('producer', None)
    validate_serializer = serializers.EventSerializer(instance=instance, data=request.data)
    validate_serializer.is_valid(raise_exception=True)
    validate_serializer.save()
    return validate_serializer.data


def destroy(request, id):
    instance = __get_one(id)
    __has_permission(request, instance)
    instance.delete()
    return


def isOwner(request, event_id):
    instance = __get_one(event_id)
    __has_permission(request, instance)
