import pytest
from api.models import UserAccount
from rest_framework.test import APIClient
from faker import Faker

client = APIClient()
faker = Faker()

# Test creation and database insertion of a single user
def test_new_user(new_user):
    assert new_user.email
    assert UserAccount.objects.all().count() == 1


@pytest.mark.django_db
def test_register_user_request():
    passwd = faker.password()
    payload = {
        "email": faker.email(),
        "name": faker.name(),
        "password": passwd,
        "re_password": passwd,
    }

    response = client.post("/auth/users/", payload)
    data = response.data

    assert data["email"] == payload["email"]
    assert data["name"] == payload["name"]
    assert payload["password"] not in data
    assert type(data["id"]) is int


# @pytest.mark.django_db
# def test_user_login():
#     # Testing successful user login
#     passwd = faker.password()
#     payload = {
#         "email": faker.email(),
#         "name": faker.name(),
#         "password": passwd,
#         "re_password": passwd,
#     }
