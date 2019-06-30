from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.views import Response

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

    @action(detail=True, methods=['GET'], url_path='amount-due', name='Get amount due contract')
    def amount_due(self, request, pk=None):
        contract = self.get_object()

        return Response({'amount_due': contract.amount_due}, status=status.HTTP_200_OK)

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
