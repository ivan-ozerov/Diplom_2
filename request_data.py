
class URLs:

    MAIN_URL = "https://stellarburgers.nomoreparties.site/api/"
    ORDERS_URL = MAIN_URL + "orders"
    ORDERS_ALL_URL = MAIN_URL + "orders/all"
    REGISTER_URL = MAIN_URL + "auth/register"
    LOGIN_URL = MAIN_URL + "auth/login"
    USER_URL = MAIN_URL + "auth/user"
    INGREDIENTS_URL =MAIN_URL + "ingredients"

class RequestHeaders:

    @staticmethod
    def get_authorization_header(access_token):
        if not access_token is None:
            return {"Authorization": access_token}
        else:
            return None
    
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

    NO_ACCESS_TOKEN__RESPONSE = {
        "success": False,
        "message": "You should be authorised"
    }

    ORDER__NO_INGREDIENTS__RESPONSE = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    ORDER__INCORRECT_HASHES__RESPONSE = {
        "success": False,
        "message": "One or more ids provided are incorrect"
    }
