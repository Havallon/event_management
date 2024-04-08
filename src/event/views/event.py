from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from person import permissions
from event.services import event_service


class ListCreateEventView(APIView):
    permission_classes = [permissions.ProducerPermission | permissions.AdminPermission]

    def get(self, request):
        events = event_service.get_all(request)
        return Response(events)

    def post(self, request):
        event = event_service.create_event(request)
        return Response(event)


class RetrieveUpdateDestroyEventView(APIView):
    permission_classes = [permissions.ProducerPermission | permissions.AdminPermission]

    def get(sef, request, pk):
        event = event_service.get_by_id(request, pk)
        return Response(event)

    def put(self, request, pk):
        event = event_service.update(request, pk)
        return Response(event)

    def delete(self, request, pk):
        event_service.destroy(request, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
