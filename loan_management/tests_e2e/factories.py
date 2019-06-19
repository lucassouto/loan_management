import factory

from ..users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda seq: f'user-{seq}')
    email = factory.LazyAttribute(lambda user: f'{user.username}@test.com')
    password = factory.PostGenerationMethodCall('set_password', 'teste')
