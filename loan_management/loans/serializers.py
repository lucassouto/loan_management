from rest_framework import serializers

from ..users.serializers import UserSerializer
from .models import Contract, Payment


class ContractSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = (
            'id',
            'client',
            'amount',
            'interest_rate',
            'ip_address',
            'bank',
            'submission_date',
        )
        read_only_fields = ('client',)

    def create(self, validated_data):
        client = self.context['request'].user

        return Contract.objects.create(client=client, **validated_data)


class PaymentSerializer(serializers.ModelSerializer):
    contract = ContractSerializer(read_only=True)
    contract_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
