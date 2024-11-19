import helper


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
        
class RequestUserUpdateData:

    new_string = 'upd2'
    EACH_FIELD_AND_ALL__PAYLOAD = [
        {
        "email": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['email']}{new_string}"
        },
        {
        "name": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['name']}{new_string}"
        },
        {
        "password": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['password']}{new_string}"
        },
        {
        "email": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['email']}{new_string}",
        "name": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['name']}{new_string}",
        "password": f"{RequestRegisterData.CORRECT_CREDENTIALS__PAYLOAD['password']}{new_string}"
        }
    ]
        
class RequestOrderData:

    CORRECT__PAYLOAD = {
        "ingredients": helper.generate_ingredients()
    }

    WITHOUT_INGREDIENTS__PAYLOAD = {
        "ingredients": []
    }

    INCORRECT_HASHES__PAYLOAD = {
        "ingredients": [
            "60d3b41abdacab0026a733c7",
            "609646e4dc916e00276b2871"
        ]
    }

    

