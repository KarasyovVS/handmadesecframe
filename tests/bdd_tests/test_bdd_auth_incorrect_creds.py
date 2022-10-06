import allure
import pytest
import time

from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.scripts import ScriptsClass
from tests.config.endpoints import Endpoints
from tests.pages.login_page import LoginPage
from tests.pages.success_login_page import SuccessLoginPage


@allure.feature("1 Идентификация и аутентификация")
@allure.story("1-2 Аутентификация в системе c некорректными УД")
@pytest.mark.parametrize("login,password", [("admin", "randomValue342"),
                                            ("randomValue1", "admin"),
                                            ("randomValue1", "randomValue1"),
                                            ("admi", "admin"),
                                            ("admin", "admi"),
                                            ("admin", "demo1234")])
@scenario(scenario_name="Аутентификация в системе",
          feature_name="feature_files/auth_test_bdd_incorrect_creds.feature")
def test_login(login, password):
    pass


@given("Открыть страницу аутентификации, ввести логин, пароль и "
       "нажать на кнопку входа")
def open_login_page(pre_conditions, login, password):
    Browser.get_browser().set_url(pre_conditions["url"] + Endpoints.AUTH_PATH)
    Logger.info(login + password)
    ScriptsClass.login_script(login=login,
                              password=password)


@then("Должно появляться сообщение об ошибке")
def success_login_page_opened():
    login_page = LoginPage()
    assert login_page.check_login_failed(), "Login is successful"
    Logger.info("Login is not successful")
