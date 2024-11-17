from methods.user_methods import UserMethods

def does_user_exists(payload):
    response = UserMethods.user_login(payload)
    if response.status_code == 200:
        return True
    else:
        return False