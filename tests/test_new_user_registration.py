from sellar_burgers_api import SellarBurgersApi
from helpers import Helpers
from data import RequestBodies, ResponseBodies
import pytest
import allure


class TestNewUserRegistration:


    @allure.title('Проверка успешной регистрации пользователя')
    @allure.description('Направляем POST запрос на ручку регистрации пользователя с корректными данными, проверяем код 200 и возврат токенов пользователя')
    def test_new_user_registration_successful(self):
        new_user_registration_response = SellarBurgersApi.new_user_registration(Helpers.registration_new_user_and_return_login_password())
        assert new_user_registration_response.status_code == 200 and ('accessToken' and 'refreshToken') in new_user_registration_response.json()



    @allure.title('Проверка регистрации пользователя с повторяющейся почтой')
    @allure.description('Направляем POST запрос на ручку регистрации пользователя с ранее используемой почтой, проверяем код и тело ответа')
    def test_repeated_user_registration_failed(self):
        new_user_registration_response = SellarBurgersApi.new_user_registration(RequestBodies.REPEATED_USER_REGISTRATION_REQUEST_BODY)
        assert new_user_registration_response.status_code == 403 and new_user_registration_response.json() == ResponseBodies.REPEATED_USER_REGISTRATION_RESPONSE_BODY



    @allure.title('Проверка регистрации пользователя без указания логина/пароля/имени')
    @allure.description('Направляем POST запрос на ручку регистрации пользователя без указания логина/пароля/имени, проверяем код и тело ответа')
    @pytest.mark.parametrize('body', [RequestBodies.USER_REGISTRATION_BODY_WITHOUT_EMAIL, RequestBodies.USER_REGISTRATION_BODY_WITHOUT_PASSWORD, RequestBodies.USER_REGISTRATION_BODY_WITHOUT_NAME])
    def test_user_registration_without_something_body_field(self, body):
        new_user_registration_response = SellarBurgersApi.new_user_registration(body)
        assert new_user_registration_response.status_code == 403 and new_user_registration_response.json() == ResponseBodies.USER_REGISTRATION_WITHOUT_SOMETHING_FIELD_RESPONSE_BODY


