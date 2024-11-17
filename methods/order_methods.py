import requests
from test_data import URLs, RequestData, RequestHeaders

class OrderMethods:

    @staticmethod
    def create_order(payload, access_token):
        response = requests.post(url=URLs.ORDERS_URL, json=payload, headers=RequestHeaders.get_authorization_header(access_token))
        return response
    
    @staticmethod
    def get_orders(access_token):
        response = requests.get(url=URLs.ORDERS_URL, headers=RequestHeaders.get_authorization_header(access_token))
        return response