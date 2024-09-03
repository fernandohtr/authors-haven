import pytest

from v1.users.forms import UserCreationForm
from v1.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_creation_form_valid_data():
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password1": "test_password",
        "password2": "test_password",
    }
    form = UserCreationForm(data)

    assert form.is_valid()


@pytest.mark.django_db
def test_user_creation_form_invalid_data():
    user = UserFactory()
    invalid_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": user.email,
        "password1": "test_password",
        "password2": "test_password",
    }
    form = UserCreationForm(invalid_data)
    assert not form.is_valid()
    assert "email" in form.errors
