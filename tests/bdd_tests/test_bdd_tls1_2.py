# import os
# import pytest

# from pytest_bdd import scenario, given, then

# from framework.browser.browser import Browser
# from framework.utils.logger import Logger
# from framework.utils.url_generator import URLGenerator
# from tests.config.urls import Urls

# @pytest.fixture(scope='function')
# def context():
#     return {}

# @scenario(scenario_name="Сканирование веб-ресурса на "
#                         "предмет поддержки протокола tls 1.2",
#           feature_name="/home/ckecker/python_frame_repo/"
#           "handmadesecframe/tests/feature_files/"
#           "tls1_2_test_bdd.feature")
# def test_tls1_2_is_used():
#     pass


# @given("Запустить проверку инструментом sslyze")
# def get_results_from_sslyze_scan(context):
#     url = URLGenerator.prepare_url_for_sslyze(Urls.TEST_STAND_URL)
#     Logger.info("Запуск sslyze по url: {}".format(url))
#     result = os.popen("sslyze {} --tlsv1_2".format(url)).read()
#     Logger.info("Результат работы sslyze: {}".format(result))
#     context["partial_result"] = result


# @then("Получено подтверждение о поддержке ненулевого количества "
#       "способов шифрования")
# def check_result(context):
#     assert "server accepted the following" in context["partial_result"], \
#         "Ресурс не поддерживает tls 1.2"
#     Logger.info("Ресурс поддерживает tls 1.2")
