class URLs:

    #base URLs
    MAIN_URL = "https://stellarburgers.nomoreparties.site/api/"
    ORDERS_URL = MAIN_URL + "orders"
    REGISTER_URL = MAIN_URL + "auth/register"
    LOGIN_URL = MAIN_URL + "auth/login"
    USER_URL = MAIN_URL + "auth/user"


class RequestRegisterData:

    CORRECT_CREDENTIALS__PAYLOAD = {
        "email": "yozhik_ya@yandex.ru",
        "password": "yozhik-123",
        "name": "yozhik"
    }

    MISSING_ONE_FIELD_CREDENTIALS__PAYLOAD = [
        {
            "email": f"{CORRECT_CREDENTIALS__PAYLOAD['email']}",
            "password": f"{CORRECT_CREDENTIALS__PAYLOAD['password']}"
        },
        {
            "email": f"{CORRECT_CREDENTIALS__PAYLOAD['email']}",
            "name": f"{CORRECT_CREDENTIALS__PAYLOAD['name']}"
        },
        {
            "name": f"{CORRECT_CREDENTIALS__PAYLOAD['name']}",
            "password": f"{CORRECT_CREDENTIALS__PAYLOAD['password']}"
        },
    ]

    ONE_FIELD_EMPTY_CREDENTIALS__PAYLOAD = [
        {
            "email": "",
            "password": f"{CORRECT_CREDENTIALS__PAYLOAD['password']}",
            "name": f"{CORRECT_CREDENTIALS__PAYLOAD['name']}"
        },
        {
            "email": f"{CORRECT_CREDENTIALS__PAYLOAD['email']}",
            "password": "",
            "name": f"{CORRECT_CREDENTIALS__PAYLOAD['name']}"
        },
        {
            "email": f"{CORRECT_CREDENTIALS__PAYLOAD['email']}",
            "password": f"{CORRECT_CREDENTIALS__PAYLOAD['password']}",
            "name": ""
        },
    ]

    
class RequestLoginData:

        CORRECT_CREDENTIALS__PAYLOAD = {
            "email": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['email']}",
            "password": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['password']}"
        }

        CHANGED_CREDENTIALS_OR_MISSING_ONE_FIELD__PAYLOAD = [
        {
            "email": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['email']}_new",
            "password": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['password']}"
        },
        {
            "email": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['email']}",
            "password": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['password']}_new"
        },
        {
            "email": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['email']}",
        },
        {
            "password": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['password']}"
        },
    ]
        
class RequestOrderData:

    CORRECT__PAYLOAD = {
        "ingredients": [
            "60d3b41abdacab0026a733c6",
            "609646e4dc916e00276b2870"
        ]
    }

    INCORRECT_HASHES__PAYLOAD = {
        "ingredients": [
            "60d3b41abdacab0026a733c7",
            "609646e4dc916e00276b2871"
        ]
    }

class RequestHeaders:

    @staticmethod
    def get_authorization_header(access_token):
        return {"Authorization": access_token}
    
class ResponseData:

    REGISTRATION__USER_ALREADY_EXIST__RESPONSE = {
        "success": False,
        "message": "User already exists"
    }

    REGISTRATION__ONE_FIELD_MISSING__RESPONSE = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    LOGIN__INCORRECT_CREDENTIALS__RESPONSE = {
        'success': False, 
        'message': 'email or password are incorrect'
    }