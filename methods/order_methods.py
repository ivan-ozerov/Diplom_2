import requests
from request_data import URLs, RequestHeaders

class OrderMethods:

    @staticmethod
    def create_order(payload, access_token=None):
        response = requests.post(url=URLs.ORDERS_URL, json=payload, headers=RequestHeaders.get_authorization_header(access_token))
        return response
    
    @staticmethod
    def get_orders(access_token=None):
        response = requests.get(url=URLs.ORDERS_URL, headers=RequestHeaders.get_authorization_header(access_token))
        return response
    
    @staticmethod
    def get_all_orders(access_token=None):
        response = requests.get(url=URLs.ORDERS_ALL_URL)
        return response
    
    @staticmethod
    def get_ingredients():
        response = requests.get(url=URLs.INGREDIENTS_URL)
        return response