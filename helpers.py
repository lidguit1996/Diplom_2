import random
import string
from sellar_burgers_api import SellarBurgersApi
import allure


class Helpers:
    @staticmethod
    @allure.step('Генерируем тело запроса для регистрации пользователя')
    def registration_new_user_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        email = generate_random_string(10) + '@yandex.ru'
        password = generate_random_string(10)
        name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload


    @staticmethod
    @allure.step('Создаем нового пользователя и берем его токен (accessToken)')
    def get_new_user_token():
        token = SellarBurgersApi.new_user_registration(Helpers.registration_new_user_and_return_login_password()).json()["accessToken"]
        return {'Authorization': str(token)}


