import factory
from faker import Faker
from faker.providers import internet
from api.models import UserAccount

faker = Faker()

class UserAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAccount

    email = faker.email(domain="gmail.com")
    is_active = "True"
