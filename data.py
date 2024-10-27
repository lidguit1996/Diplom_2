class Urls:
    URL_MAIN = "https://stellarburgers.nomoreparties.site/"
    ORDERS_ALL_ENDPOINT = "api/orders/all"
    NEW_USER_REGISTRATION_ENDPOINT = "api/auth/register"
    USER_LOGIN_ENDPOINT = "api/auth/login"
    USER_LOGOUT_ENDPOINT = "api/auth/logout"
    UPDATE_USER_DATA_ENDPOINT = "api/auth/user"
    ORDER_CREATION_ENDPOINT = "api/orders"
    GET_USER_ORDERS_ENDPOINT = "api/orders"

class RequestBodies:

    REPEATED_USER_REGISTRATION_REQUEST_BODY = {"email": "yurikhanalaynen@yandex.ru", "password": "password", "name": "Username"}
    USER_REGISTRATION_BODY_WITHOUT_EMAIL = {"password": "password", "name": "Username"}
    USER_REGISTRATION_BODY_WITHOUT_PASSWORD = {"email": "yurikhanalaynen@yandex.ru", "name": "Username"}
    USER_REGISTRATION_BODY_WITHOUT_NAME = {"email": "yurikhanalaynen@yandex.ru", "password": "password"}
    USER_LOGIN_CORRECT_BODY = {"email": "yurikhanalaynen@yandex.ru", "password": "password"}
    USER_LOGIN_BODY_WITH_INVALID_EMAIL = {"email": "yurikhanalaynen12345@yandex.ru", "password": "password"}
    USER_LOGIN_BODY_WITH_INVALID_PASSWORD = {"email": "yurikhanalaynen@yandex.ru", "password": "password1234"}
    ORDER_CORRECT_INGREDIENTS_BODY = {"ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa71"]}
    ORDER_BODY_WITH_EMPTY_LIST = {"ingredients": []}
    EMPTY_BODY = {}
    ORDER_INVALID_HASH_INGREDIENT_BODY = {"ingredients": ["абвгдеёжз"]}




class ResponseBodies:

    REPEATED_USER_REGISTRATION_RESPONSE_BODY = {"success": False, "message": "User already exists"}
    USER_REGISTRATION_WITHOUT_SOMETHING_FIELD_RESPONSE_BODY = {"success": False, "message": "Email, password and name are required fields"}
    USER_LOGIN_WITH_INVALID_LOGIN_OR_PASSWORD_RESPONSE_BODY = {"success": False, "message": "email or password are incorrect"}
    UPDATE_USER_DATA_WITHOUT_AUTHORISATION_RESPONSE_BODY = {"success": False,"message": "You should be authorised"}
    ORDER_WITHOUT_INGREDIENTS_RESPONSE_BODY = {"success": False, "message": "Ingredient ids must be provided"}
    GET_USER_ORDER_WITHOUT_AUTHORISATION_RESPONSE_BODY = {"success": False, "message": "You should be authorised"}






