# Дипломный проект, задание №2 - API тесты для покрытия сайта Stellar Burgers 

## Покрытые эндпоинты

api/orders
api/ingredients
api/auth/register
api/auth/login
api/auth/user

## Структура проекта

.
├── allure-report                                   - allure отчет
├── allure-results                                  - allure результаты
├── conftest.py                                     - фикстура создания и удаления пользователя
├── helper.py                                       - вспомогательные функции
├── methods                                         - api методы
├── request_data.py                                 - ожидаемые результаты и другие данные
├── requirements.txt                                - зависимости
├── test_data.py                                    - тестовые данные
└── tests                                           - тесты
├── order                                           - тесты заказов
    │   ├── test_order_create.py
    │   └── test_orders_get.py
└── user                                            - тесты пользователей
        ├── test_user_login.py
        ├── test_user_register.py
        └── test_user_update.py

10 directories, 88 files

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание результов тестирования**

> `$ python -m pytest --alluredir=allure-results`

**Создание HTML-отчета на основании результатов тестирования**

> `$ allure generate allure-results` и
> `$ allure open allure-report` 
или
> `$ allure serve allure-results` 
