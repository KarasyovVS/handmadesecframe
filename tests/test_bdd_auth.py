import time

from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.config.paths import Paths
from tests.config.urls import Urls
from tests.pages.login_page import LoginPage
from tests.pages.success_login_page import SuccessLoginPage

@scenario(scenario_name="login attempt", feature_name=
"/Users/vladimirkarasev/Desktop/handmadesecframe/tests/"
"authorization_test_bdd.feature")
def test_login():
    pass

@given("open login page")
def open_login_page(create_browser):
    Browser.get_browser().set_url(Urls.TEST_STAND_URL + Paths.AUTH_PATH)
    login_page = LoginPage()
    assert login_page.is_opened(), "Login page is not opened"
    Logger.info("Login page is opened")

@given("fill in login and password and click login button")
def authorization():
    login_page = LoginPage()
    login_page.authorizate("admin", "admin")

@then("I should see success login page")
def success_login_page_opened():
    success_login_page = SuccessLoginPage()
    assert success_login_page.is_opened(), "Login is not successful"
    Logger.info("Login is successful")
    time.sleep(5)
