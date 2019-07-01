import factory

from .models import Bank


class BankFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bank

    name = 'Banco do Brasil'
    tax_identification = '001'
