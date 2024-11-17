from methods.user_methods import UserMethods
from test_data import RequestLoginData, ResponseData
import pytest

class TestUserLogin:

    def test_user_login_correct_credentials(self, user_creation):
        response = UserMethods.user_login(RequestLoginData.CORRECT_CREDENTIALS__PAYLOAD)
        assert response.status_code == 200 and 'accessToken' in response.json()

    @pytest.mark.parametrize("payload", RequestLoginData.CHANGED_CREDENTIALS_OR_MISSING_ONE_FIELD__PAYLOAD)
    def test_user_login_incorrect_credentials(self, user_creation, payload):
        response = UserMethods.user_login(payload)
        print(response.text)
        assert response.status_code == 401 and response.json() == ResponseData.LOGIN__INCORRECT_CREDENTIALS__RESPONSE

    