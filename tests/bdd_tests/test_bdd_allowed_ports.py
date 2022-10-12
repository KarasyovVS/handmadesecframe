import pytest
import allure

from pytest_bdd import scenario, given, then

from framework.utils.logger import Logger
from framework.utils.nmap_func import NmapFunctions
from framework.utils.url_generator import URLGenerator
from tests.config.nmap_configs.ports import Ports


@pytest.fixture(scope='function')
def context():
    return {}

@allure.feature("5 Дополнительные точки входа")
@allure.story("5-6 Сканирование открытых портов")
@scenario(scenario_name="Сканирование веб-ресурса на наличие открытых портов",
          feature_name="feature_files/allowed_ports_test_bdd.feature")
def test_allowed_ports_is_used():
    pass


@given("Запустить проверку инструментом nmap")
def get_results_from_nmap(pre_conditions, context):
    url = pre_conditions["url"]
    url = URLGenerator.prepare_url_for_nmap_scan(url)
    Logger.info("Запуск nmap по url: {url}".format(url=url))
    result = NmapFunctions.execute_nmap_scan(url=url, ports=Ports.PORTS_RANGE)
    context["partial_result"] = result


@then("Получено подтверждение о соответствии открытых портов только разрешенным")
def check_result(context):
    assert NmapFunctions.validate_scan_results(
        result=context["partial_result"],
        allowed_ports_list=Ports.ALLOWED_PORTS)[0], \
        "Открытые порты не соответствуют заявленным"
    Logger.info("Открытые порты соответствуют заявленным")
