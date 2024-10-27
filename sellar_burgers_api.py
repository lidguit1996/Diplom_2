import allure
import requests
from data import Urls

class SellarBurgersApi:


    @staticmethod
    @allure.step('Направляем POST запрос на регистрацию пользователя')
    def new_user_registration(payload):
        return requests.post(Urls.URL_MAIN + Urls.NEW_USER_REGISTRATION_ENDPOINT, data=payload)


    @staticmethod
    @allure.step('Направляем POST запрос на ручку авторизации пользователя')
    def user_login(payload):
        return requests.post(Urls.URL_MAIN + Urls.USER_LOGIN_ENDPOINT,data=payload)


    @staticmethod
    @allure.step('Направляем PACTH запрос на ручку изменения данных пользователя')
    def update_user_data(token, payload):
        return requests.patch(Urls.URL_MAIN + Urls.UPDATE_USER_DATA_ENDPOINT, headers=token, data=payload)


    @staticmethod
    @allure.step('Направляем POST запрос на ручку создания нового заказа')
    def order_creation(token, payload):
        return requests.post(Urls.URL_MAIN + Urls.ORDER_CREATION_ENDPOINT, headers=token, data=payload)


    @staticmethod
    @allure.step('Направляем GET запрос на ручку получения заказа пользователя')
    def get_user_orders(token):
        return requests.get(Urls.URL_MAIN + Urls.GET_USER_ORDERS_ENDPOINT, headers=token)






