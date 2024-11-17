from methods.user_methods import UserMethods
from test_data import RequestRegisterData, ResponseData
import pytest

class TestUserRegister:

    def test_user_register_correct_credentials(self, user_creation):
        assert user_creation.status_code == 200 and "accessToken" in user_creation.json()

    def test_user_register_already_exist(self, user_creation):
        response = UserMethods.user_registration(RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD)
        assert response.status_code == 403 and response.json() == ResponseData.REGISTRATION__USER_ALREADY_EXIST__RESPONSE

    @pytest.mark.parametrize("payload", RequestRegisterData.MISSING_ONE_FIELD_CREDENTIALS__PAYLOAD)
    def test_user_register_missing_one_field(self, payload):
        response = UserMethods.user_registration(payload)
        assert response.status_code == 403 and response.json() == ResponseData.REGISTRATION__ONE_FIELD_MISSING__RESPONSE

