from sellar_burgers_api import SellarBurgersApi
from helpers import Helpers
from data import ResponseBodies
import allure



class TestGetUserOrders:

    @allure.title('Проверка запроса на получение данных заказа авторизованным пользователем')
    @allure.description('Направляем GET запрос на ручку получения данных заказа авторизованного пользователя (с указанием токена), проверяем код и тело ответа')
    def test_get_user_orders(self):
        get_user_orders_response = SellarBurgersApi.get_user_orders(Helpers.get_new_user_token())
        assert get_user_orders_response.status_code == 200 and ("success" and "orders" and "total" and "totalToday") in get_user_orders_response.json() and get_user_orders_response.json()["success"] == True



    @allure.title('Проверка запроса на получение данных заказа неавторизованным пользователем')
    @allure.description('Направляем GET запрос на ручку получения данных заказа неавторизованным пользователем (без указания токена), проверяем код и тело ответа')
    def test_get_user_orders_without_authorisation(self):
        get_user_orders_response = SellarBurgersApi.get_user_orders({})
        assert get_user_orders_response.status_code == 401 and get_user_orders_response.json() == ResponseBodies.GET_USER_ORDER_WITHOUT_AUTHORISATION_RESPONSE_BODY