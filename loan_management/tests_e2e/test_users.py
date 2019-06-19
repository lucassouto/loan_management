import pytest

from django.conf import settings
from django.urls import reverse


@pytest.mark.django_db
def test_get_users(client, token):
    url = settings.BASE_URL + reverse('api:users:users-list')
    response = client.get(url, headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 200
