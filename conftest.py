from test_data import RequestRegisterData, RequestLoginData
from methods.user_methods import UserMethods
import pytest
import helper
import allure


@pytest.fixture
@allure.title("Preparation: creating (or login) and deleting user")
def user_creation():
    with allure.step("Setup: Determining whether a user is in the system or not"):
        if not helper.does_user_exists(RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD):
            with allure.step("Setup: User creation"):
                response = UserMethods.user_registration(RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD)
        else:
            with allure.step("Setup: User login"):
                response = UserMethods.user_login(RequestLoginData.CORRECT_CREDENTIALS__PAYLOAD)
    yield response
    with allure.step("Teardown: User deletion"):
        response_delete = UserMethods.user_deletion(response.json()["accessToken"])
    assert response_delete.status_code == 202