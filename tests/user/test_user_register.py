from methods.user_methods import UserMethods
from test_data import RequestRegisterData
from request_data import ResponseData
import pytest
import allure

@allure.parent_suite("API Tests")
@allure.suite("User Tests")
@allure.sub_suite("User Registration Tests")
class TestUserRegister:

    @allure.title("User registration with correct credentials")
    def test_user_register_correct_credentials(self, user_creation):
        assert user_creation.status_code == 200 and "accessToken" in user_creation.json()

    @allure.title("User registration, which already exist")
    def test_user_register_already_exist(self, user_creation):
        response = UserMethods.user_registration(RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD)
        assert response.status_code == 403 and ResponseData.REGISTRATION__USER_ALREADY_EXIST__RESPONSE['message'] in response.json()['message']

    @allure.title("User registration, missing one field")
    @pytest.mark.parametrize("payload", RequestRegisterData.MISSING_ONE_FIELD_CREDENTIALS__PAYLOAD)
    def test_user_register_missing_one_field(self, payload):
        response = UserMethods.user_registration(payload)
        assert response.status_code == 403 and ResponseData.REGISTRATION__ONE_FIELD_MISSING__RESPONSE['message'] in response.json()['message']

