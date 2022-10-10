import subprocess

from framework.utils.logger import Logger
from tests.config.nuclei_configs.fuzzing_templates import FuzzingTemplates


class NucleiFunctions(object):


    NUCLEI_SCAN_CMD = "nuclei -u {url} {options}"


    @staticmethod
    def validate_scan_results(scan_result: str) -> bool:
        if "No results found" not in scan_result:
            Logger.info(scan_result)
            return False
        return True


    @classmethod
    def execute_nuclei_scan(cls, url: str, options: str) -> str:
        nuclei_cmd = cls.NUCLEI_SCAN_CMD.format(url=url, options=options)
        result = (subprocess.Popen(nuclei_cmd, shell=True, 
                                     stderr=subprocess.PIPE)).communicate()
        return result[-1].decode("utf-8")
    

    @classmethod
    def get_fuzzing_results(cls, url: str, 
                            excluded_templates=
                                FuzzingTemplates.EXCLUDED_TEMPLATES) -> str:
        fuzz_options = " ".join([FuzzingTemplates.ALL_TEMPLATES_CMD, 
                                 FuzzingTemplates.EXCLUDE_TEMPLATES_CMD.format(
                                        templates=excluded_templates
                                    )])
        return cls.execute_nuclei_scan(url, fuzz_options)
