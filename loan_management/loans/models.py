import uuid

from django.db import models
from model_utils.models import TimeStampedModel

from ..banks.models import Bank
from ..users.models import User


class Contract(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    interest_rate = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    submission_date = models.DateTimeField()
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, related_name='contracts')
    client = models.ForeignKey(User, on_delete=models.PROTECT, related_name='contracts')


class Payment(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_date = models.DateTimeField()
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT, related_name='payments')
