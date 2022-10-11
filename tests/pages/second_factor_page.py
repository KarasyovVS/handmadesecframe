from selenium.webdriver.common.by import By

from framework.pages.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text_box import TextBox


class SecondFactorPage(BasePage):

    SEARCH_CONDITION = By.XPATH
    
    SOME_LOC = ""
    SECOND_FACTOR_TB_LOC = ""
    CONFIRM_BTN_LOC = ""

    def __init__(self):
        super().__init__(search_condition=self.SEARCH_CONDITION,
                         locator=self.SOME_LOC,
                         page_name=self.__class__.__name__)

    def fill_in_second_factor(self, second_factor):
        second_factor_tb = TextBox(search_condition=self.SEARCH_CONDITION,
                                   locator=self.SECOND_FACTOR_TB_LOC, 
                                   name="Second factor text box")
        second_factor_tb.send_keys_without_click(second_factor, hide_logs=True)
    
    def send_second_factor(self, second_factor):
        self.fill_in_second_factor(second_factor)
        confirm_btn = Button(search_condition=self.SEARCH_CONDITION,
                             locator=self.CONFIRM_BTN_LOC,
                             name="Confirm button")
        confirm_btn.click()
