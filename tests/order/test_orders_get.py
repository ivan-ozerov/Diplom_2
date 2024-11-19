from methods.order_methods import OrderMethods
from test_data import RequestOrderData
from request_data import ResponseData
import pytest
import allure

@allure.parent_suite("API Tests")
@allure.suite("Order Tests")
@allure.sub_suite("Order Get Tests")
class TestOrderGet:

    @allure.title("Get specific user orders")
    def test_get_orders(self, user_creation):
        response = OrderMethods.get_orders(user_creation.json()["accessToken"])
        assert response.status_code == 200

    @allure.title("Get orders without token of cpecific user")
    def test_get_orders_without_token(self):
        response = OrderMethods.get_orders()
        assert response.status_code == 401 and response.json()['message'] in ResponseData.NO_ACCESS_TOKEN__RESPONSE['message']

    @allure.title("Create order and get orders of cpecific user")
    def test_create_order_and_get_orders(seldf, user_creation):
        response = OrderMethods.create_order(RequestOrderData.CORRECT__PAYLOAD)
        response = OrderMethods.get_orders(user_creation.json()['accessToken'])
        # assert response.status_code == 200 and response.json()['total'] != 0

    