import time

from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.config.urls import Urls
from tests.config.paths import Paths
from tests.pages.login_page import LoginPage
from tests.pages.success_login_page import SuccessLoginPage
from tests.scripts import ScriptsClass


@scenario(scenario_name="Аутентификация в системе", 
          feature_name="/home/developer1/handmadesecframe/tests"
          "/feature_files/auth_test_bdd.feature")
def test_login():
    pass


@given("Открыть страницу аутентификации, ввести логин, пароль и "
       "нажать на кнопку входа")
def open_login_page(create_browser):
    Browser.get_browser().set_url(Urls.TEST_STAND_URL + Paths.AUTH_PATH)
    ScriptsClass.login_script(login="admin", password="admin")


@then("Должна открыться страница успешной аутентификации")
def success_login_page_opened():
    success_login_page = SuccessLoginPage()
    assert success_login_page.is_opened(), "Login is not successful"
    Logger.info("Login is successful")
