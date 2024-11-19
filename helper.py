from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods  
import random


def does_user_exists(payload):
    response = UserMethods.user_login(payload)
    if response.status_code == 200:
        return True
    else:
        return False
    
def generate_ingredients():
    ingredients_ids = []
    ingredients = OrderMethods.get_ingredients().json()['data']
    ingredients_number = random.randint(1, len(ingredients))
    for i in range(ingredients_number):
        id = ingredients[random.randint(0, len(ingredients)-1)]['_id']
        ingredients_ids.append(id)
    return ingredients_ids

