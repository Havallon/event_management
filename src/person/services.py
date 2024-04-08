from rest_framework.request import Request
from person.models import Person
from person.serializers import PersonSerializer, CreatePersonSerializer


def get_all() -> list:
    queryset = Person.objects.all()
    serializer = PersonSerializer(queryset, many=True)
    return serializer.data


def create_person(request: Request) -> dict:
    validate_serializer = CreatePersonSerializer(data=request.data)
    validate_serializer.is_valid(raise_exception=True)
    person = Person.objects.create_user(**validate_serializer.validated_data)
    serializer = PersonSerializer(person)
    return serializer.data
