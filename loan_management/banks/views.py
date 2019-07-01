from rest_framework import permissions, viewsets

from .models import Bank
from .serializers import BankSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAdminUser]
