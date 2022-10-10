import allure
import pytest
import time

from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.scripts import ScriptsClass
from tests.config.config_test_file import TestConfigs
from tests.config.endpoints import Endpoints
from tests.pages.login_page import LoginPage
from tests.pages.success_login_page import SuccessLoginPage


@allure.feature("1 Идентификация и аутентификация")
@allure.story("1-2 Аутентификация в системе c некорректными УД -"
              "максимальное количество попыток входа c некорректным паролем")
@scenario(scenario_name="Аутентификация в системе заданное количество раз"
                        " с некорректным паролем",
          feature_name="feature_files/"
                       "auth_test_bdd_incorrect_creds_max_retries.feature")
def test_login():
    pass


@given("Открыть страницу аутентификации, ввести корректный логин, "
       "некорректный пароль и нажать на кнопку входа, должно появляться "
       "сообщение об ошибке. Повторить заданное количество раз +1")
def open_login_page(pre_conditions):
    Browser.get_browser().set_url(pre_conditions["url"] + Endpoints.AUTH_PATH)
    for _ in range(TestConfigs.MAX_AUTH_RETRIES):
        ScriptsClass.login_script(login="jsmith", password="randomValue342")
        login_page = LoginPage()
        assert login_page.check_login_failed(), "Login is successful"
        Logger.info("Login is not successful")


@then("Появляется сообщение о блокировке УЗ")
def success_login_page_opened():
    login_page = LoginPage()
    success_login_page = SuccessLoginPage()
    assert login_page.check_account_blocked_message() or \
        not success_login_page.is_opened, "Account is available"
    Logger.info("Acoount is blocked")
