import factory
from faker import Faker

from .models import User

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.simple_profile()['username']
    email = factory.LazyAttribute(lambda user: f'{user.username}@test.com')
    password = fake.password()
