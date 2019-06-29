from decimal import Decimal

import pytest
from django.urls import reverse
from django.utils import timezone
from faker import Faker

from .factories import UserFactory

fake = Faker()


@pytest.mark.django_db
def test_get_contracts(client, contract):
    client.force_login(user=contract.client)

    response = client.get(reverse('api:loans:contracts-list'))

    assert response.status_code == 200
    assert len(response.json()['results']) == 1


@pytest.mark.django_db
def test_get_contracts_user_not_authorized(client, contract):
    user = contract.client
    user_not_authorized = UserFactory(username='not_authorized')

    client.force_login(user=user_not_authorized)

    response = client.get(reverse('api:loans:contracts-list'))

    assert user.contracts.count() != len(response.json()['results'])


@pytest.mark.django_db
def test_post_contracts(client, bank, user):
    client.force_login(user=user)

    data = {
        'amount': fake.pydecimal(left_digits=4, right_digits=2, positive=True),
        'interest_rate': 0.2,
        'ip_address': fake.ipv4_private(),
        'submission_date': fake.date_time(tzinfo=timezone.utc),
        'bank': bank.id,
        'client': user.id,
    }

    response = client.post(reverse('api:loans:contracts-list'), data=data)

    assert response.status_code == 201
    assert user.contracts.count() == 1


@pytest.mark.django_db
def test_delete_contracts(client, contract):
    client.force_login(user=contract.client)

    response = client.delete(reverse('api:loans:contracts-detail', kwargs={'pk': contract.id}))

    assert response.status_code == 405


@pytest.mark.django_db
def test_get_payments(client, payment):
    client.force_login(user=payment.contract.client)

    response = client.get(reverse('api:loans:payments-list'))

    assert response.status_code == 200
    assert len(response.json()['results']) == 1


@pytest.mark.django_db
def test_post_payments(client, contract):
    client.force_login(user=contract.client)

    data = {
        'payment_date': fake.date_time(tzinfo=timezone.utc),
        'payment_amount': fake.pydecimal(left_digits=4, right_digits=2, positive=True),
        'contract': contract.id,
    }

    response = client.post(reverse('api:loans:payments-list'), data=data)

    assert response.status_code == 201
    assert contract.payments.count() == 1


@pytest.mark.django_db
def test_delete_payments(client, payment):
    client.force_login(user=payment.contract.client)

    response = client.delete(reverse('api:loans:payments-detail', kwargs={'pk': payment.id}))

    assert response.status_code == 405


@pytest.mark.django_db
def test_get_amount_due_contract(client, contract, payment):
    client.force_login(user=contract.client)

    response = client.get(reverse('api:loans:contracts-amount-due', kwargs={'pk': contract.id}))

    assert response.status_code == 200

    assert contract.amount_due == round(Decimal(response.json()['amount_due']), 2)
