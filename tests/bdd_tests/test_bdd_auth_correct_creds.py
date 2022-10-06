import allure
import time

from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from framework.utils.random_generator import RandomGenerator
from tests.config.endpoints import Endpoints
from tests.pages.login_page import LoginPage
from tests.pages.second_factor_page import SecondFactorPage
from tests.pages.success_login_page import SuccessLoginPage
from tests.scripts import ScriptsClass


@allure.feature("1 Идентификация и аутентификация")
@allure.story("1-1 Аутентификация в системе с корректными УД")
@scenario(scenario_name="Аутентификация в системе", 
          feature_name="feature_files/auth_test_bdd.feature")
def test_login():
    pass


@given("Открыть страницу аутентификации, ввести логин, пароль и "
       "нажать на кнопку входа")
def open_login_page(pre_conditions):
    Browser.get_browser().set_url(pre_conditions["url"] + Endpoints.AUTH_PATH)
    ScriptsClass.login_script(login="admin", password="admin")


@then("Должна открыться страница успешной аутентификации " 
      "или страница ввода второго фактора")
def success_login_page_opened(pre_conditions):
    if pre_conditions["2fa"]:
        second_factor_page = SecondFactorPage()
        assert second_factor_page.is_opened(), \
            "Страница ввода второго фактора не открыта"
        Logger.info("Страница ввода второго фактора открыта")
        second_factor_page.send_second_factor(
            RandomGenerator.get_random_string(length=6))
        assert second_factor_page.is_opened(), \
            "Страница ввода второго фактора не открыта"
        Logger.info("Страница ввода второго фактора открыта")
    else:
        success_login_page = SuccessLoginPage()
        assert success_login_page.is_opened(), "Аутентификация не успешна"
        Logger.info("Аутентификация успешна")
