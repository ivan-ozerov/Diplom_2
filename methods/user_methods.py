
import requests
from test_data import URLs, RequestHeaders


class UserMethods:

    @staticmethod
    def user_registration(payload):
        response = requests.post(url=URLs.REGISTER_URL, json=payload)
        return response
    
    @staticmethod
    def user_deletion(access_token):
        response = requests.delete(url=URLs.USER_URL, headers=RequestHeaders.get_authorization_header(access_token))
        return response
    
    @staticmethod
    def user_login(payload):
        response = requests.post(URLs.LOGIN_URL, json=payload)
        return response
    
    @staticmethod
    def user_update(payload, access_token):
        response = requests.patch(URLs.USER_URL, json=payload, headers=RequestHeaders.get_authorization_header(access_token))
        return response
    
