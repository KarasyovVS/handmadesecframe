# coding=utf-8
from selenium.common.exceptions import StaleElementReferenceException

from framework.constants import page_states
from framework.constants.js_scripts import JSScripts


class WaitForReadyStateComplete(object):
    def __init__(self, browser):
        self.browser = browser

    def __call__(self, driver):
        try:
            return self.browser.execute_script(
                JSScripts.GET_PAGE_READY_STATE) == page_states.COMPLETE
        except StaleElementReferenceException:
            return False
