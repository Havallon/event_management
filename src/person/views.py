from rest_framework import status
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


class RetrieveUpdateDestroyPersonView(APIView):
    permission_classes = [permissions.AdminPermission]

    def get(self, request, pk):
        person = services.get_by_id(pk)
        return Response(person)

    def put(self, request, pk):
        person = services.update(request, pk)
        return Response(person)

    def patch(self, request, pk):
        person = services.partial_update(request, pk)
        return Response(person)

    def delete(self, request, pk):
        services.destroy(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
