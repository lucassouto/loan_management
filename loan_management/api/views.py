from rest_framework import status, viewsets
from rest_framework.response import Response


class HealthCheck(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'healthy'}, status=status.HTTP_200_OK)
