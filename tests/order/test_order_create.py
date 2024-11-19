from methods.order_methods import OrderMethods
from test_data import RequestOrderData
from request_data import ResponseData
import pytest
import allure

@allure.parent_suite("API Tests")
@allure.suite("Order Tests")
@allure.sub_suite("Order Creation Tests")
class TestOrderCreate:

    @allure.title("Create order with ingredients")
    def test_create_order_with_ingredients(self, user_creation):
        response = OrderMethods.create_order(RequestOrderData.CORRECT__PAYLOAD)
        print(response.text)
        assert response.status_code == 200 and 'order' in response.json()

    @allure.title("Create order without ingredients")
    def test_create_order_without_ingredients(self, user_creation):
        response = OrderMethods.create_order(RequestOrderData.WITHOUT_INGREDIENTS__PAYLOAD)
        print(response.text)
        assert response.status_code == 400 and ResponseData.ORDER__NO_INGREDIENTS__RESPONSE['message'] in response.json()['message']

    @allure.title("Create order with ingredients with incorrect hashes")
    def test_create_order_with_incorrect_hashes(self, user_creation):
        response = OrderMethods.create_order(RequestOrderData.INCORRECT_HASHES__PAYLOAD)
        print(response.text)
        assert response.status_code == 400 and ResponseData.ORDER__INCORRECT_HASHES__RESPONSE['message'] in response.json()['message']

    @allure.title("Create order with token")
    def test_create_order_with_token(self, user_creation):
        response = OrderMethods.create_order(RequestOrderData.CORRECT__PAYLOAD, user_creation.json()["accessToken"])
        print(response.text)
        assert response.status_code == 200 and 'order' in response.json()

