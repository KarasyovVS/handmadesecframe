from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage


class LandingPage(BasePage):

    SEARCH_CONDITION = By.XPATH

    TABLE_FIELD_LOC = "//table//td//tr//td"

    def __init__(self):
        super().__init__(search_condition=self.SEARCH_CONDITION,
                         locator=self.TABLE_FIELD_LOC,
                         page_name=self.__class__.__name__)
