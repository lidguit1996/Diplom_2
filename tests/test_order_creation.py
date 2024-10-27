from sellar_burgers_api import SellarBurgersApi
from helpers import Helpers
from data import RequestBodies, ResponseBodies
import pytest
import allure


class TestOrderCreation:

    @allure.title('Проверка запроса на создание заказа авторизованным пользователем')
    @allure.description('Направляем POST запрос на ручку создания заказа с указанием токена, проверяем код и тело ответа ')
    def test_order_creation_with_authorisation(self):
        order_creation_response = SellarBurgersApi.order_creation(Helpers.get_new_user_token(), RequestBodies.ORDER_CORRECT_INGREDIENTS_BODY)
        assert order_creation_response.status_code == 200 and ("success" and "name" and "order") in order_creation_response.json() and order_creation_response.json()["success"] == True



    @allure.title('Проверка запроса на создание заказа неавторизованным пользователем')
    @allure.description('Направляем POST запрос на ручку создания заказа без указания токена, проверяем код и тело ответа')
    def test_order_creation_without_authorisation(self):
        order_creation_response = SellarBurgersApi.order_creation({}, RequestBodies.ORDER_CORRECT_INGREDIENTS_BODY)
        assert order_creation_response.status_code == 200 and ("success" and "name" and "order") in order_creation_response.json() and order_creation_response.json()["success"] == True



    @allure.title('Проверка запроса на создание заказа без указания ингредиентов')
    @allure.description('Направляем POST запрос на ручку создания заказа без указания ингредиента либо с пустым телом запроса, проверяем код и тело ответа')
    @pytest.mark.parametrize('ingredients', [RequestBodies.ORDER_BODY_WITH_EMPTY_LIST, RequestBodies.EMPTY_BODY])
    def test_order_creation_without_ingredients(self, ingredients):
        order_creation_response = SellarBurgersApi.order_creation(Helpers.get_new_user_token(), ingredients)
        assert order_creation_response.status_code == 400 and order_creation_response.json() == ResponseBodies.ORDER_WITHOUT_INGREDIENTS_RESPONSE_BODY



    @allure.title('Проверка запроса на создание заказа с несуществующим ингредиентом')
    @allure.description('Направляем POST запрос на ручку создания с указанием неверного хэша ингредиента, проверяем код и тело ответа')
    def test_order_creation_with_invalid_ingredient_hash(self):
        order_creation_response = SellarBurgersApi.order_creation(Helpers.get_new_user_token(), RequestBodies.ORDER_INVALID_HASH_INGREDIENT_BODY)
        assert order_creation_response.status_code == 500