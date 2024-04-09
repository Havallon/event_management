from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from event.services import section_service


class ListCreateSectionhView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, event_id):
        sections = section_service.get_all(event_id)
        return Response(sections)

    def post(self, request, event_id):
        section = section_service.create_section(request, event_id)
        return Response(section)


class RetrieveUpdateDestroySectionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        section = section_service.get_by_id(pk)
        return Response(section)

    def put(self, request, pk):
        section = section_service.update(request, pk)
        return Response(section)

    def delete(self, request, pk):
        section_service.destroy(request, pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
