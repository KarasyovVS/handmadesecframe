import pytest
import allure

from pytest_bdd import scenario, given, then

from framework.utils.nmap_func import NmapFunctions
from framework.utils.logger import Logger
from framework.utils.url_generator import URLGenerator
from framework.constants import nmap_scripts
from tests.config.nmap_configs.ports import Ports
from tests.config.nmap_configs.certification_authority import \
    CertificationAuthority as cert


@pytest.fixture(scope='function')
def context():
    return {}


@allure.feature("6 Безопасность транспорта")
@allure.story("6-1 HTTPS")
@scenario(scenario_name="Сканирование веб-ресурса на "
                        "предмет поддержки протокола tls 1.2",
          feature_name="feature_files/tls1_2_test_bdd.feature")
def test_tls1_2_is_used():
    pass


@given("Запустить проверку инструментом nmap")
def get_results_from_nmap_scan(pre_conditions, context):
    ports = Ports.SSL_PORT
    ssl_cert_script = nmap_scripts.Scripts.SSL_CERT
    url = pre_conditions["url"]
    url = URLGenerator.prepare_url_for_nmap_scan(url)
    Logger.info("Запуск nmap по url: {url}".format(url=url))
    result = NmapFunctions.execute_nmap_script_scan(ports=ports, script=ssl_cert_script, url=url)
    context["partial_result"] = result


@then("Получено подтверждение о поддержке ненулевого количества "
      "способов шифрования")
def check_result(context):
    assert NmapFunctions.validate_ssl_cert_scan_results(
        result=context["partial_result"], CA=cert.GPN_CA), \
        "Ресурс не поддерживает tls 1.2"
    Logger.info("Ресурс поддерживает tls 1.2")
