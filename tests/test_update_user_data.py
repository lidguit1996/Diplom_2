from sellar_burgers_api import SellarBurgersApi
from helpers import Helpers
from data import ResponseBodies
import allure



class TestUpdateUserData:

    @allure.title('Проверка запроса изменения данных авторизованного пользователя')
    @allure.description('Направляем PATCH запрос на ручку изменений данных пользователя с корректным токеном, проверяем код и тело ответа')
    def test_update_user_data_successful(self):
        update_user_data_response = SellarBurgersApi.update_user_data(Helpers.get_new_user_token(), Helpers.registration_new_user_and_return_login_password())
        assert update_user_data_response.status_code == 200 and update_user_data_response.json()["success"] == True



    @allure.title('Проверка запроса изменения данных неавторизованного пользователя')
    @allure.description('Направляем PATCH запрос на ручку изменений данных пользователя без токена, проверяем код и тело ответа')
    def test_update_user_data_without_authorisation(self):
        update_user_data_response = SellarBurgersApi.update_user_data({}, Helpers.registration_new_user_and_return_login_password())
        assert update_user_data_response.status_code == 401 and update_user_data_response.json() == ResponseBodies.UPDATE_USER_DATA_WITHOUT_AUTHORISATION_RESPONSE_BODY


