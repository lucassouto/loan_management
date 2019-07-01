from decimal import Decimal

import factory
from django.utils import timezone
from faker import Faker

from ..banks.factories import BankFactory
from ..loans.models import Contract, Payment
from ..users.factories import UserFactory

fake = Faker()


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    amount = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    interest_rate = Decimal(0.2)
    ip_address = fake.ipv4_private()
    submission_date = fake.date_time(tzinfo=timezone.utc)
    bank = factory.SubFactory(BankFactory)
    client = factory.SubFactory(UserFactory)


class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment

    payment_date = fake.date_time(tzinfo=timezone.utc)
    payment_amount = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    contract = factory.SubFactory(ContractFactory)
