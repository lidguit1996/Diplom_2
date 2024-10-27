from sellar_burgers_api import SellarBurgersApi
from data import RequestBodies, ResponseBodies
import pytest
import allure


class TestUserLogin:

    @allure.title('Проверка запроса логина пользователя с валидными данными')
    @allure.description('Направляем POST запрос на ручку логина пользователя с валидными почтой и паролем в теле, проверяем код 200 и возврат токенов пользователя')
    def test_user_login_successful(self):
        user_login_response = SellarBurgersApi.user_login(RequestBodies.USER_LOGIN_CORRECT_BODY)
        assert user_login_response.status_code == 200 and ('accessToken' and 'refreshToken') in user_login_response.json()



    @allure.title('Проверка запроса логина пользователя с неверной почтой либо паролем')
    @allure.description('Направляем POST запрос на ручку логина пользователя с некорректным логином либо паролем, проверяем код и тело овтета')
    @pytest.mark.parametrize('body', [RequestBodies.USER_LOGIN_BODY_WITH_INVALID_EMAIL, RequestBodies.USER_LOGIN_BODY_WITH_INVALID_PASSWORD])
    def test_user_login_with_invalid_login_or_password(self, body):
        user_login_response = SellarBurgersApi.user_login(body)
        assert user_login_response.status_code == 401 and user_login_response.json() == ResponseBodies.USER_LOGIN_WITH_INVALID_LOGIN_OR_PASSWORD_RESPONSE_BODY