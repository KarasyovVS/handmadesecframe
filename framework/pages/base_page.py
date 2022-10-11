from abc import ABC
from enum import unique

from framework.browser.browser import Browser
from framework.elements.label import Label
from framework.utils.logger import Logger


class BasePage(ABC):
    def __init__(self, search_condition, locator, page_name):
        self.locator = locator
        self.page_name = page_name
        self.SEARCH_CONDITION = search_condition

    def wait_page_to_load(self):
        Logger.info(
            "Ожидание загрузки страницы {page_name} методами js".format(
                page_name=self.page_name))
        Browser.get_browser().wait_for_page_to_load()

    def is_opened(self):
        Logger.info("Проверка на отображение {page_name}".format(
            page_name=self.page_name))
        self.wait_page_to_load()
        return Browser.get_browser().is_wait_successful(
            Label(self.SEARCH_CONDITION, self.locator,
                  self.page_name).wait_for_is_visible)

    def wait_for_page_closed(self):
        self.wait_page_to_load()
        return Browser.get_browser().is_wait_successful(
            Label(self.SEARCH_CONDITION, self.locator,
                  self.page_name).wait_for_is_absent)
    
    def is_closed(self):
        Logger.info("Проверка отсутствия уникального элемента на странице")
        unique_elem = Label(self.SEARCH_CONDITION, self.locator,
                            self.page_name)
        return not unique_elem.get_elements()

    def wait_for_page_opened(self):
        Logger.info(
            "Ожидание загрузки страницы {page_name} и видимости "
            "идентифицирующего ее элемента".format(page_name=self.page_name))
        self.wait_page_to_load()
        Label(self.SEARCH_CONDITION, self.locator,
              self.page_name).wait_for_is_visible()

    def refresh_page(self):
        Logger.info("Обновление страницы {page_name}".format(
            page_name=self.page_name))
        Browser.get_browser().refresh_page()
