import pytest


@pytest.fixture()
def auth_client(client, django_user_model):
    django_user_model.objects.create_user(username='lucas', password='teste')

    client.login(username='lucas', password='teste')
    return client
