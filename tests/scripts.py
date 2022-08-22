from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.pages.login_page import LoginPage


class ScriptsClass:

    @classmethod
    def login_script(self, login, password):
        login_page = LoginPage()
        assert login_page.is_opened(), "Login page is not opened"
        Logger.info("Login page is opened")
        login_page.authorizate(login, password)
