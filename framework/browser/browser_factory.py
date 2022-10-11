from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests.config.browser import BrowserConfig
from framework.constants.browsers import Browsers


class BrowserFactory(object):

    @staticmethod
    def get_browser_driver():
        if BrowserConfig.BROWSER == Browsers.BROWSER_CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            return webdriver.Chrome(ChromeDriverManager().install(),
                                    options=chrome_options)
