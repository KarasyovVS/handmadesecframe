import time

from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.scripts import ScriptsClass
from tests.config.paths import Paths
from tests.config.urls import Urls
from tests.pages.login_page import LoginPage
from tests.pages.success_login_page import SuccessLoginPage


@scenario(scenario_name="Аутентификация в системе",
          feature_name="/home/developer1/handmadesecframe/tests"
          "/feature_files/auth_test_bdd_incorrect_creds.feature")
def test_login():
    pass


@given("Открыть страницу аутентификации, ввести логин, пароль и "
       "нажать на кнопку входа")
def open_login_page(create_browser):
    Browser.get_browser().set_url(Urls.TEST_STAND_URL + Paths.AUTH_PATH)
    ScriptsClass.login_script(login="randomValue194",
                              password="randomValue342")


@then("Должно появляться сообщение об ошибке")
def success_login_page_opened():
    login_page = LoginPage()
    assert login_page.check_login_failed(), "Login is successful"
    Logger.info("Login is not successful")
