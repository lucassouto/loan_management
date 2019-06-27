from rest_framework import permissions, status, viewsets
from rest_framework.response import Response


class HealthCheck(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)

    def list(self, request):
        return Response({'message': 'healthy'}, status=status.HTTP_200_OK)
