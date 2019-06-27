import pytest
from django.urls import reverse
from faker import Faker

fake = Faker()


@pytest.mark.django_db
def test_get_contracts(auth_client):
    response = auth_client.get(reverse('api:loans:contracts-list'))

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_contracts(auth_client, bank, user):
    data = {
        'amount': fake.pydecimal(left_digits=4, right_digits=2, positive=True),
        'interest_rate': 1,
        'ip_address': fake.ipv4_private(),
        'submission_date': fake.date_time(),
        'bank': bank.id,
        'client': user.id,
    }

    response = auth_client.post(reverse('api:loans:contracts-list'), data=data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_delete_contracts(auth_client, contract):
    response = auth_client.delete(reverse('api:loans:contracts-detail', kwargs={'pk': contract.id}))

    assert response.status_code == 204
