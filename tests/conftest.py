from email.policy import default
import pytest

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from tests.config.browser import BrowserConfig


def pytest_addoption(parser):
    parser.addoption("--browser", action="store",
                     default=BrowserConfig.BROWSER,
                     help="Name of browser")
    parser.addoption("--login", action="store",
                     default="defaultLogin",
                     help="Login for authentication")
    parser.addoption("--password", action="store",
                     default="defaultPassword",
                     help="Password for authentication")
    parser.addoption("--url", action="store",
                     default="noUrl",
                     help="Password for authentication")
    parser.addoption("--2fa", action="store",
                     default=False,
                     help="Two factor authentication in system")


@pytest.fixture(scope="session")
def pre_conditions(request):

    browser = request.config.getoption("--browser")
    Browser.get_browser().set_up_driver(browser_key=browser)
    Browser.get_browser().maximize(browser_key=browser)
    Logger.info("==============MAIN TEST PART==============")

    yield {"url": request.config.getoption("--url"), 
           "2fa": request.config.getoption("--2fa")}

    Logger.info("==============MAIN TEST PART==============")
    for browser_key in list(Browser.get_browser().get_driver_names()):
        Browser.get_browser().quit(browser_key=browser_key)
