from pytest_factoryboy import register

from .factories import BankFactory, ContractFactory, PaymentFactory, UserFactory

register(BankFactory)
register(ContractFactory)
register(PaymentFactory)
register(UserFactory)
