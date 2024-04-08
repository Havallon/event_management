from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from person import permissions, services


class ListCreatePersonView(APIView):

    def get(self, request: Request) -> Response:
        permissions.is_admin(request, self)
        people = services.get_all()
        return Response(people)

    def post(self, request: Request) -> Response:
        person = services.create_person(request)
        return Response(person)
