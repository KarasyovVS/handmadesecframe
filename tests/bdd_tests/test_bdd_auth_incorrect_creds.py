import allure
import pytest

from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.scripts import ScriptsClass
from tests.config.creds_file import Creds
from tests.config.endpoints import Endpoints
from tests.pages.login_page import LoginPage


@allure.feature("1 Идентификация и аутентификация")
@allure.story("1-2 Аутентификация в системе c некорректными УД")
@pytest.mark.parametrize("login,password", Creds.INCORRECT_CREDS)
@scenario(scenario_name="Аутентификация в системе",
          feature_name="feature_files/auth_test_bdd_incorrect_creds.feature")
def test_login(login, password):
    pass


@given("Открыть страницу аутентификации, ввести логин, пароль и "
       "нажать на кнопку входа")
def open_login_page(pre_conditions, login, password):
    Browser.get_browser().set_url(pre_conditions["url"] + Endpoints.AUTH_PATH)
    ScriptsClass.login_script(login=login,
                              password=password)


@then("Должно появляться сообщение об ошибке")
def success_login_page_opened():
    login_page = LoginPage()
    assert login_page.check_login_failed(), "Аутентификация успешна"
    Logger.info("Аутентификация не успешна")
