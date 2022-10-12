import allure
import pytest

from pytest_bdd import scenario, given, then

from framework.browser.browser import Browser
from framework.storages.local_storage import LocalStorage
from framework.utils.logger import Logger
from tests.pages.success_login_page import SuccessLoginPage
from tests.scripts import ScriptsClass
from tests.config.creds_file import Creds
from tests.config.endpoints import Endpoints
from tests.pages.login_page import LoginPage


@pytest.fixture(scope='function')
def context():
    return []


@allure.feature("7 Безопасность браузера")
@allure.story("7-10 Чувствительная информация в local storage")
@pytest.mark.parametrize("creds", Creds.CORRECT_CREDS)
@scenario(scenario_name="Проверка локального хранилища",
          feature_name="feature_files/sensible_info_in_local_storage.feature")
def test_local_storage(creds):
    pass


@given("Авторизоваться в системе под определенной ролью, заполнить "
       "формы приложения чувствительной информацией")
def log_in_and_fill_in_forms(pre_conditions, creds, context):
    Browser.get_browser().set_url(pre_conditions["url"] + Endpoints.AUTH_PATH)
    ScriptsClass.login_script(login=creds["login"],
                              password=creds["password"])
    success_login_page = SuccessLoginPage()
    assert success_login_page.is_opened(), "Аутентификация не успешна"
    Logger.info("Аутентификация успешна")
    # Тут д.б. заполнение форм чувствительной инфо и сохранение ее в переменную context
    context.append(creds["login"])
    context.append(creds["password"])


@then("Проверить содержимое локального хранилища на отсутствие чувствительной"
      " информации")
def check_local_storage(context):
    local_storage = LocalStorage()
    for elem in local_storage.items():
        for sens_info in context:
            assert not sens_info in elem, "Чувствительная информация " \
                "сохранена в локальном хранилище: {sens_info}".format(
                    sens_info=str(local_storage.items()))
    Logger.info("Локальное хранилище не содержит чувствительных данных")
