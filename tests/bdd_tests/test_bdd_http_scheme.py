from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.utils.logger import Logger
from framework.utils.url_generator import URLGenerator
from tests.config.urls import Urls
from tests.pages.landing_page import LandingPage


@scenario(scenario_name="Переход по URL ресурса с невалидной схемой",
          feature_name="/home/ckecker/python_frame_repo/"
          "handmadesecframe/tests/feature_files/"
          "http_test_bdd.feature")
def test_main_page_opened():
    pass


@given("Открыть главную страницу веб-ресурса, используя схему http")
def open_landing_page_with_http_scheme(create_browser):
    http_url = URLGenerator.switch_https_to_http(Urls.TEST_STAND_URL)
    Browser.get_browser().set_url(http_url)
    landing_page = LandingPage()


@then("Переход по URL со схемой http безрезультатен")
def check_landing_page_is_not_opened():
    landing_page = LandingPage()
    page_not_opened = landing_page.wait_for_page_closed()
    url_contains_https = URLGenerator.url_contains_https(
        Browser.get_browser().get_current_url())
    assert page_not_opened or url_contains_https, "Переход по URL со " \
                                                  "схемой http успешен"
    if page_not_opened:
        Logger.info("Переход по URL со схемой http безрезультатен")
    else:
        Logger.info("При переходе по URL со схемой http веб-ресурс"
                    " осуществляет редирект на URL со схемой https")
