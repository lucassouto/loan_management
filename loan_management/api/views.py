from rest_framework import status, viewsets
from rest_framework.response import Response


class HelloProject(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'Hello Project!!!'}, status=status.HTTP_200_OK)
