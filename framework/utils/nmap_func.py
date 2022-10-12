import subprocess

from framework.utils.logger import Logger


class NmapFunctions(object):

    NMAP_SCAN_CMD = "nmap -p {ports} {url}"

    @staticmethod
    def validate_scan_results(result: str, allowed_ports_list: list) -> tuple:
        opened_list = []
        filtered_list = []
        result = result.split("\n")
        for elem in result[4:]:
            if "open" in elem:
                opened_list.append(elem)
            elif "filtered" in elem:
                filtered_list.append(elem)
        for i in opened_list.copy():
            for j in allowed_ports_list.copy():
                if j in i:
                    allowed_ports_list.remove(j)
                    opened_list.remove(i)
        if len(opened_list) + len(allowed_ports_list) != 0:
            Logger.info("Open ports left: {opened_list}; "
                        "Allowed ports left: {allowed_ports_list}".\
                        format(opened_list=str(opened_list),
                               allowed_ports_list=str(allowed_ports_list)))
            return False, filtered_list
        return True, filtered_list


    @classmethod
    def execute_nmap_scan(cls, url: str, ports: str) -> str:
        nmap_cmd = cls.NMAP_SCAN_CMD.format(ports=ports, url=url)
        result = (subprocess.Popen(nmap_cmd, shell=True,
                                   stdout=subprocess.PIPE)).communicate()
        return result[0].decode("utf-8")
