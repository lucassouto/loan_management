from django.urls import reverse


def test_health_api(client):
    response = client.get(reverse('api:health_check-list'))

    assert response.status_code == 200
