import pytest
from api.models import UserAccount

# Test creation and database insertion of a single user
def test_new_user(new_user):
    assert new_user.email
    assert UserAccount.objects.all().count() == 1
