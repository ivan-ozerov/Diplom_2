from methods.user_methods import UserMethods
from test_data import RequestRegisterData, RequestUserUpdateData
from request_data import ResponseData
import pytest
import allure

@allure.parent_suite("API Tests")
@allure.suite("User Tests")
@allure.sub_suite("User Update Tests")
class TestUserUpdate:

    @allure.title("User update with correct data")
    @allure.description("Update each field individually and all together")
    @pytest.mark.parametrize("payload", RequestUserUpdateData.EACH_FIELD_AND_ALL__PAYLOAD)
    def test_user_update_correct_data(self, user_creation, payload):
        response = UserMethods.user_update(payload, user_creation.json()["accessToken"])
        assert response.status_code == 200
        
    @allure.title("User update without access token")
    def test_user_update_without_access_token(self, user_creation):
        response = UserMethods.user_update(RequestUserUpdateData.EACH_FIELD_AND_ALL__PAYLOAD[-1])
        assert response.status_code == 401 and ResponseData.NO_ACCESS_TOKEN__RESPONSE['message'] in response.json()['message']

    