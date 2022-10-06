import os
from unittest import result

from framework.utils.logger import Logger


class NucleiFunctions(object):

    # Целевое виденье
    # FUZZ_WITH_TEMPLATE_CMD = "nuclei -u {url} -itags fuzz -t {template_path}"

    # Временное решение
    FUZZ_WITH_TEMPLATE_CMD = "sudo docker run --name {cont_name} " \
                             "8a8c5465105b -u {url} " \
                             "-itags fuzz -t {template_path}"
    GET_DOCKER_LOGS_CMD = "sudo docker container logs {cont_name}"


    @staticmethod
    def validate_scan_results(scan_result: dict) -> bool:
        for elem in scan_result:
            Logger.info(scan_result[elem])
            if "no results found" not in scan_result[elem].lower:
                Logger.info(scan_result)
                return False
        return True


    @staticmethod
    def nuclei_scanning_with_templates_list(url: str, templates_list: list, 
                                            scanning_func) -> list:
        result = []
        for template in templates_list:
            result.append(scanning_func(url, template))
        return result


    @staticmethod
    def nuclei_fuzzing_scan(url: str, template_path: str) -> dict:
        cont_name = template_path.split("/")[-1]
        nuclei_cmd = NucleiFunctions.FUZZ_WITH_TEMPLATE_CMD.format(url=url, 
            template_path=template_path, cont_name=cont_name)
        get_logs_from_container_cmd = NucleiFunctions.GET_DOCKER_LOGS_CMD.\
            format(cont_name=cont_name)
        os.popen(nuclei_cmd)
        result = os.popen(get_logs_from_container_cmd).read()
        Logger.info(str(result))
        return {nuclei_cmd: result}
