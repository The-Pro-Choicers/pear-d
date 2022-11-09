import pytest

from pytest_factoryboy import register
from tests.factories import UserAccountFactory

register(UserAccountFactory)

@pytest.fixture
def new_user(db, user_account_factory):
    user = user_account_factory.create()
    return user
