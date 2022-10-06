from selenium.webdriver.common.by import By

from framework.elements.button import Button
from framework.elements.label import Label
from framework.elements.text_box import TextBox
from framework.pages.base_page import BasePage


class LoginPage(BasePage):

    SEARCH_CONDITION = By.XPATH

    LOGIN_TEXT_LOC = "//h1[contains(text(), 'Online Banking Login')]"
    LOGIN_TB_LOC = "//input[@id='uid']"
    PASSW_TB_LOC = "//input[@id='passw']"
    LOGIN_BTN_LOC = "//input[contains(@type, 'ubmit') and contains(@value, " \
                    "'ogin')]"
    LOGIN_FAILED_TXT_LOC = "//span[contains(text(), 'was not found')]"
    ACCOUNT_BLOCKED_TXT_LOC = "//div[contains(text(), 'account is blocked')]"

    def __init__(self):
        super().__init__(search_condition=self.SEARCH_CONDITION,
                         locator=self.LOGIN_TEXT_LOC,
                         page_name=self.__class__.__name__)

    def fill_in_login(self, login):
        login_tb = TextBox(search_condition=self.SEARCH_CONDITION,
                           locator=self.LOGIN_TB_LOC, name="Login text box")
        login_tb.send_keys_without_click(login, hide_logs=True)

    def fill_in_password(self, password):
        password_tb = TextBox(search_condition=self.SEARCH_CONDITION,
                              locator=self.PASSW_TB_LOC,
                              name="Password text box")
        password_tb.send_keys_without_click(password, hide_logs=True)

    def authorizate(self, login, password):
        self.fill_in_login(login)
        self.fill_in_password(password)
        login_btn = Button(search_condition=self.SEARCH_CONDITION,
                           locator=self.LOGIN_BTN_LOC, name="Login button")
        login_btn.click()

    def check_login_failed(self):
        login_failed_text = Label(search_condition=self.SEARCH_CONDITION,
                                  locator=self.LOGIN_FAILED_TXT_LOC,
                                  name="Login failed text")
        if login_failed_text.is_displayed():
            return True
        else:
            return False
    
    def check_account_blocked_message(self):
        account_blocked_text = Label(search_condition=self.SEARCH_CONDITION,
                                     locator=self.ACCOUNT_BLOCKED_TXT_LOC,
                                     name="Account blocked text")
        if account_blocked_text.is_displayed():
            return True
        else:
            return False
