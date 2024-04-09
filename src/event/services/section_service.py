from rest_framework import exceptions
from event import models, serializers
from event.services import event_service


def __get_one(id):
    try:
        queryset = models.Section.objects.get(id=id)
        return queryset
    except models.Section.DoesNotExist:
        raise exceptions.NotFound('Section not found')


def get_all(event_id) -> list:
    queryset = models.Section.objects.filter(event__id=event_id)
    serializer = serializers.SectionSerializer(queryset, many=True)
    return serializer.data


def create_section(request, event_id) -> dict:
    event_service.isOwner(request, event_id)
    request.data['event'] = event_id
    validate_serializer = serializers.SectionSerializer(data=request.data)
    validate_serializer.is_valid(raise_exception=True)
    validate_serializer.save()
    return validate_serializer.data


def get_by_id(id):
    section = __get_one(id)
    serializer = serializers.SectionSerializer(section)
    return serializer.data


def __has_permission(request, section):
    if section.event.producer == request.user:
        return
    raise exceptions.PermissionDenied('This Section isnt yours')


def update(request, id):
    instance = __get_one(id)
    __has_permission(request, instance)
    request.data.pop('event', None)
    validate_serializer = serializers.SectionSerializer(instance=instance, data=request.data)
    validate_serializer.is_valid(raise_exception=True)
    validate_serializer.save()
    return validate_serializer.data


def destroy(request, id):
    instance = __get_one(id)
    __has_permission(request, instance)
    instance.delete()
    return
