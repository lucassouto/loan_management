from pytest_factoryboy import register

from loan_management.banks.factories import BankFactory
from loan_management.loans.factories import ContractFactory, PaymentFactory
from loan_management.users.factories import UserFactory

register(BankFactory)
register(ContractFactory)
register(PaymentFactory)
register(UserFactory)
