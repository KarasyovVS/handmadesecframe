import allure
import pytest

from pytest_bdd import scenario, given, then

from framework.constants import nmap_scripts
from framework.utils.logger import Logger
from framework.utils.nmap_func import NmapFunctions
from framework.utils.url_generator import URLGenerator
from tests.config.nmap_configs.certification_authority import \
    CertificationAuthority as CertAuthor
from tests.config.nmap_configs.ports import Ports


@pytest.fixture(scope="function")
def context():
    return {}


@allure.feature("6 Безопасность транспорта")
@allure.story("6-1 Цифровой сертификат")
@scenario(scenario_name="Сканирование веб-ресурса для получения "
                        "информации о сертификате",
          feature_name="feature_files/cert_ca_date_test_bdd.feature")
def test_cert_ca_date():
    pass


@given("Запустить проверку инструментом nmap")
def get_results_from_nmap_scan(pre_conditions, context):
    url = pre_conditions["url"]
    url = URLGenerator.prepare_url_for_nmap_scan(url)
    Logger.info("Запуск nmap по url: {url}".format(url=url))
    result = NmapFunctions.execute_nmap_script_scan(
        ports=Ports.SSL_PORT, script=nmap_scripts.Scripts.SSL_CERT, url=url)
    context["partial_result"] = result


@then("Получено подтверждение, что сертификат выпустил одобренный "
      "Центр сертификации и срок действия сертификата не истек")
def check_result(context):
    assert NmapFunctions.validate_cert_ca_date_scan_results(
        result=context["partial_result"], approved_ca=CertAuthor.GPN_CA), \
        "Удостоверяющий центр и срок действия сертификата не валидны"
    Logger.info("Удостоверяющий центр и срок действия сертификата валидны")
