from selenium.common.exceptions import NoSuchWindowException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.config.waits import Waits
from tests.config.browser import BrowserConfig
from framework.browser.browser_factory import BrowserFactory
from framework.utils.logger import Logger
from framework.utils.url_generator import URLGenerator
from framework.waits.wait_for_custom_event import WaitForCustomEvent
from framework.waits.wait_for_ready_state_complete import \
    WaitForReadyStateComplete
from framework.waits.wait_for_true_with_action import WaitForTrueWithAction
from framework.singleton import Singleton


class Browser(metaclass=Singleton):
    def __init__(self):
        self.__web_driver = {}
        self.__main_window_handle = None
        self.__selected_browser = BrowserConfig.BROWSER

    @classmethod
    def get_browser(cls):
        return Browser()

    def get_selected_browser_key(self):
        return self.__selected_browser

    def get_browser_keys(self):
        return self.__web_driver.keys()

    def get_driver(self):
        return self.__web_driver[self.__selected_browser]

    def set_up_driver(self, browser_key=BrowserConfig.BROWSER):
        Logger.debug(
            'Инициализация драйвер для браузера ' + BrowserConfig.BROWSER)
        if browser_key in self.__web_driver:
            raise ValueError(
                "Браузер с  ключом '{browser_key}', уже создан.".format(
                    browser_key=browser_key))
        self.__web_driver[browser_key] = BrowserFactory.get_browser_driver()
        self.__web_driver[browser_key].implicitly_wait(
            Waits.IMPLICITLY_WAIT_SEC)
        self.__web_driver[browser_key].set_page_load_timeout(
            Waits.PAGE_LOAD_TIMEOUT_SEC)
        self.__web_driver[browser_key].set_script_timeout(
            Waits.SCRIPT_TIMEOUT_SEC)
        self.__main_window_handle = self.__web_driver[
            browser_key].current_window_handle
        self.select_browser(browser_key)

    def select_browser(self, browser_key=BrowserConfig.BROWSER):
        if browser_key not in self.__web_driver:
            raise KeyError(
                "Браузер с  ключом '{browser_key}', не существует.".format(
                    browser_key=browser_key))
        self.__selected_browser = browser_key

    def quit(self, browser_key=BrowserConfig.BROWSER):
        browser_inst = self.__web_driver.get(browser_key)
        if browser_inst is not None:
            Logger.debug("Прекращение работы драйвера")
            browser_inst.quit()
            self.__web_driver.pop(browser_key, None)

    def get_driver_names(self):
        return self.__web_driver.keys()

    def close(self, page_name=""):
        if self.get_driver() is not None:
            Logger.info("Закрытие страницы {name} ".format(name=page_name))
            self.get_driver().close()

    def refresh_page(self):
        Logger.info("Обновление текущей страницы")
        self.get_driver().refresh()

    def maximize(self, browser_key=BrowserConfig.BROWSER):
        self.__web_driver[browser_key].maximize_window()

    def set_url(self, url, login=None, password=None):
        Logger.info("Переход по url {}".format(url))
        if login is not None and password is not None:
            self.get_driver().get(URLGenerator.generate_url_for_basic_auth(
                url, login, password))
        else:
            self.get_driver().get(url)

    def execute_script(self, script, arguments=None):
        if arguments is None:
            arguments = []
        return self.get_driver().execute_script(script, arguments)

    def get_cookies(self):
        Logger.info("Получение всех cookies")
        return self.get_driver().get_cookies()

    def get_cookie(self, name):
        Logger.info("Получение cookie с именем: {}".format(name=name))
        return self.get_driver().get_cookie(name=name)

    def add_cookie(self, name, value):
        Logger.info("Добавление cookie с именем: '{name}'".format(name=name))
        cookie_dict = {"name": str(name), "value": str(value)}
        return self.get_driver().add_cookie(cookie_dict)

    def get_current_url(self):
        Logger.info("Получение текущего url")
        return self.get_driver().current_url

    def back_page(self):
        Logger.info("Возврат на предыдущую страницу")
        self.get_driver().back()

    def switch_to_window(self, window_handle=None):
        if window_handle is None:
            window_handle = self.__main_window_handle
        Logger.info("Переключение на вкладку {name}".format(
            name=window_handle))
        try:
            self.get_driver().switch_to.window(window_handle)
        except NoSuchWindowException:
            Logger.error(
                "Вкладка с именем {name} отсутствует".format(
                    name=window_handle))

    def __switch_alert(self):
        try:
            WebDriverWait(self.get_driver(), Waits.PAGE_LOAD_TIMEOUT_SEC).\
                until(EC.alert_is_present())
            alert = self.get_driver().switch_to.alert
            return alert
        except TimeoutException:
            Logger.error("Алерт отсутствует")
            raise TimeoutException

    def send_text_to_alert(self, text):
        Logger.info("Отправка текста '{text}' в алерт".format(text=text))
        self.__switch_alert().send_keys(text)

    def switch_to_frame_by_name(self, frame_name):
        Logger.info("Переключение на фрейм с именем {name}".format(
            name=frame_name))
        self.get_driver().switch_to_frame(frame_name)

    def switch_to_frame_by_locator(self, search_condition, locator):
        Logger.info("Переключение на фрейм локатором {loc}".format(
            loc=locator))
        self.get_driver().switch_to.frame(
            self.get_driver().find_element(search_condition, locator))

    def switch_to_default_content(self):
        Logger.info("Переключение на главный фрейм")
        self.get_driver().switch_to.default_content()

    def wait_for_page_to_load(self):
        WebDriverWait(self.get_driver(), Waits.PAGE_LOAD_TIMEOUT_SEC).until(
            WaitForReadyStateComplete(browser=self))

    def wait_for_custom_event(self, event, expected_result, *args,
                              time_in_seconds=Waits.IMPLICITLY_WAIT_SEC,
                              msg=""):
        waiter = WaitForCustomEvent(event, expected_result, *args)
        self.wait_for_check_by_condition(waiter=waiter,
                                         time_in_seconds=time_in_seconds,
                                         message=msg)

    def wait_for_true(self, expression,
                      time_in_seconds=Waits.IMPLICITLY_WAIT_SEC, msg=""):
        self.wait_for_custom_event(expression, True,
                                   time_in_seconds=time_in_seconds, msg=msg)

    def wait_for_true_with_action(self, expression, event,
                                  expression_args=None, action_args=None,
                                  time_in_seconds=Waits.IMPLICITLY_WAIT_SEC,
                                  msg=""):
        waiter = WaitForTrueWithAction(self.get_driver(), expression, event,
                                       expression_args=expression_args,
                                       action_args=action_args)
        self.wait_for_check_by_condition(waiter=waiter,
                                         time_in_seconds=time_in_seconds,
                                         message=msg)

    def wait_for_check_by_condition(self, waiter,
                                    time_in_seconds=Waits.IMPLICITLY_WAIT_SEC,
                                    message=""):
        try:
            WebDriverWait(self.get_driver(), time_in_seconds).until(waiter)
        except TimeoutException:
            error_msg = "По истечении {time} секунд не выполнено событие:" \
                        " {msg}".format(time=time_in_seconds, msg=message)
            Logger.warning(error_msg)
            raise TimeoutException(error_msg)

    def is_wait_successful(self, wait_function, *args):
        try:
            wait_function(*args)
        except TimeoutException:
            return False
        return True

    def take_a_screenshot(self, file_name):
        Logger.info("Фиксация скриншота")
        self.get_driver().save_screenshot(file_name)
        Logger.info("скриншот сохранен в файле с именем: \
                    '" + file_name + "'")
