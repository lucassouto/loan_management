import factory
from django.utils import timezone
from faker import Faker

from ..banks.models import Bank
from ..loans.models import Contract, Payment
from ..users.models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.simple_profile()['username']
    email = factory.LazyAttribute(lambda user: f'{user.username}@test.com')
    password = fake.password()


class BankFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bank

    name = 'Banco do Brasil'
    tax_identification = '001'


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    amount = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    interest_rate = 1
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
