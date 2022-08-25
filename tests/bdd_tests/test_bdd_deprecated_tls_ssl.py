import time
import os
import pytest

from pytest_bdd import scenario, given, then

from framework.utils.logger import Logger
from framework.utils.url_generator import URLGenerator
from tests.config.urls import Urls

@pytest.fixture(scope='function')
def context():
    return {}

@scenario(scenario_name="Сканирование веб-ресурса на предмет поддержки "\
                        "протоколов tls 1.1, 1, ssl 2, 3",
          feature_name="/home/ckecker/python_frame_repo/"
          "handmadesecframe/tests/feature_files/"
          "deprecated_tls_ssl_test_bdd.feature")
def test_deprecated_tls_ssl_are_not_used():
    pass


@given("Запустить проверку инструментом sslyze")
def get_results_from_sslyze_scan(context):
    url = URLGenerator.prepare_url_for_sslyze(Urls.TEST_STAND_URL)
    Logger.info("Запуск sslyze по url: {}".format(url))
    result = os.popen("sslyze {} --sslv2 --sslv3 --tlsv1 --tlsv1_1".\
        format(url)).read()
    Logger.info("Результат работы sslyze: {}".format(result))
    context["partial_result"] = result


@then("Получено подтверждение об отсутствии поддержки перечисленных "
      "протоколов")
def check_result(context):
    assert "server accepted the following" not in context["partial_result"], \
        "Ресурс поддерживает неактуальные протоколы"
    Logger.info("Ресурс не поддерживает неактуальные протоколы")
