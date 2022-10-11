import pytest
import subprocess

from pytest_bdd import scenario, given, then

from framework.utils.logger import Logger
from tests.config.ip_ports import IpAddress

@pytest.fixture(scope='function')
def context():
    return {}

@scenario(scenario_name="Сканирование веб-ресурса на наличие открытых портов",
          feature_name="feature_files/allowed_ports_test_bdd.feature")
def test_allowed_ports_is_used():
    pass


@given("Запустить проверку инструментом nmap")
def get_results_from_nmap(context):
    ip = IpAddress.TEST_STAND_IP
    Logger.info("Запуск sslyze по url: {ip}".format(ip=ip))
    result = subprocess.Popen("nmap -p 1-65535 {ip}".format(ip=ip), shell=True, stdout=subprocess.PIPE).communicate()
    result = result[0].decode("utf-8")
    Logger.info("Результат работы sslyze: {}".format(result))
    context["partial_result"] = result


@then("Получено подтверждение об открытие только разрешенных портов")
def check_result(context):
    assert "server accepted the following" in context["partial_result"], \
        "Ресурс не поддерживает tls 1.2"
    Logger.info("Ресурс поддерживает tls 1.2")
