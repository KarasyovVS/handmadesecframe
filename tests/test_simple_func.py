import time

import pytest

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.config.paths import Paths
from tests.config.urls import Urls
from tests.pages.login_page import LoginPage
from tests.pages.success_login_page import SuccessLoginPage


class TestSimpleFunc(object):

    @pytest.mark.parametrize("login,password,test_passed",
                             [("admin", "admin", True),
                              ("value1", "value2", False)])
    def test_authorization(self, create_browser, login, password, test_passed):
        Browser.get_browser().set_url(Urls.TEST_STAND_URL + Paths.AUTH_PATH)
        login_page = LoginPage()
        assert login_page.is_opened(), "Login page is not opened"
        Logger.info("Login page is opened")
        login_page.authorizate(login, password)
        if test_passed:
            success_login_page = SuccessLoginPage()
            assert success_login_page.is_opened(), "Login is not successful"
            Logger.info("Login is successful")
        else:
            assert login_page.check_login_failed(), "Login is successful"
            Logger.info("Login is not successful")

        # time.sleep(3)
