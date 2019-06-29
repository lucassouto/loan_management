from rest_framework import mixins, viewsets

from .models import Contract, Payment
from .serializers import ContractSerializer, PaymentSerializer


class ContractViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def get_queryset(self):
        return self.queryset.filter(client=self.request.user)


class PaymentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        return self.queryset.filter(contract__client=self.request.user)
