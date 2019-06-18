import requests

from django.conf import settings
from django.urls import reverse


def test_health_api():
    url = settings.BASE_URL + reverse('api:health_check-list')
    response = requests.get(url)

    assert response.status_code == 200
