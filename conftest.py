from test_data import RequestRegisterData, RequestLoginData
from methods.user_methods import UserMethods
import pytest
import helper

@pytest.fixture
def user_creation():
    if not helper.does_user_exists(RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD):
        response = UserMethods.user_registration(RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD)
    else:
        response = UserMethods.user_login(RequestLoginData.CORRECT_CREDENTIALS__PAYLOAD)
    yield response
    response_delete = UserMethods.user_deletion(response.json()["accessToken"])
    assert response_delete.status_code == 202