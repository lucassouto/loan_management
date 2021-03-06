import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_users(admin_client):
    response = admin_client.get(reverse('api:users:users-list'))

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_users(admin_client):
    response = admin_client.post(
        reverse('api:users:users-list'), data={'username': 'teste_post', 'password': 'teste'}
    )

    assert response.status_code == 201


@pytest.mark.django_db
def test_delete_users(admin_client, django_user_model):
    user = django_user_model.objects.create_user(username='teste_delete', password='teste')
    response = admin_client.delete(reverse('api:users:users-detail', kwargs={'pk': user.id}))

    assert response.status_code == 204
