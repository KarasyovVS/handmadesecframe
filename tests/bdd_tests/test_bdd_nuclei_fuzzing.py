import pytest
import allure

from pytest_bdd import scenario, given, then

from framework.utils.logger import Logger
from framework.utils.nuclei_funcs import NucleiFunctions


@pytest.fixture(scope='function')
def context():
    return {}


@allure.feature("4 Фаззинг")
@allure.story("4-1 Фаззинг форм ввода")
@scenario(scenario_name="Фаззинг веб-ресурса инструментом nuclei "\
                        "по встроенным темплейтам",
          feature_name="feature_files/fuzzing_nuclei.feature")
def test_no_vulnerables_found_by_nuclei_fuzzing():
    pass


@given("Запустить фаззинг веб-ресурса инструментом nuclei")
def get_results_from_nuclei_fuzzing(pre_conditions, context):
    url = pre_conditions["url"]
    Logger.info("Запуск nuclei по url: {}".format(url))
    context["partial_result"] = NucleiFunctions.get_fuzzing_results(url)


@then("Уязвимости инструментом nuclei не обнаружены")
def check_result(context):
    assert NucleiFunctions.validate_scan_results(context["partial_result"]), \
        "Ресурс имеет уязвимости, выявленные в процессе фаззинга"
    Logger.info("Ресурс не имеет уязвимостей, выявленных в процессе фаззинга")
