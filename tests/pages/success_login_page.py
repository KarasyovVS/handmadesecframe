from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage


class SuccessLoginPage(BasePage):

    SEARCH_CONDITION = By.XPATH

    CONGRATULATIONS_TEXT_LOC = "//h2[contains(text(), 'gratu')]"

    def __init__(self):
        super().__init__(search_condition=self.SEARCH_CONDITION,
                         locator=self.CONGRATULATIONS_TEXT_LOC,
                         page_name=self.__class__.__name__)
