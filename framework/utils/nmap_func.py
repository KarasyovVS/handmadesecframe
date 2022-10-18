import subprocess

from datetime import datetime
from framework.utils.logger import Logger


class NmapFunctions(object):
    NMAP_SCAN_CMD = 'nmap {option} {url}'
    PORTS_FLAG_CMD = '-p {ports}'
    SCRIPT_FLAG_CMD = '--script {script}'

    @staticmethod
    def validate_open_ports_scan_results(result: str, allowed_ports_list: list) -> tuple:
        opened_list = []
        filtered_list = []
        result = result.split("\n")
        for elem in result[4:]:
            if 'open' in elem:
                opened_list.append(elem)
            elif 'filtered' in elem:
                filtered_list.append(elem)
        for i in opened_list.copy():
            for j in allowed_ports_list.copy():
                if j in i:
                    allowed_ports_list.remove(j)
                    opened_list.remove(i)
        if len(opened_list) + len(allowed_ports_list) != 0:
            Logger.info('Open ports left: {opened_list}; '
                        'Allowed ports left: {allowed_ports_list}'. \
                        format(opened_list=str(opened_list),
                               allowed_ports_list=str(allowed_ports_list)))
            return False, filtered_list
        return True, filtered_list

    @staticmethod
    def validate_ssl_cert_scan_results(result: str, CA: str) -> bool:
        server_date = datetime.now()
        cert_expiration_date = NmapFunctions.__get_cert_date(result)
        if CA not in result:
            Logger.info('Удостоверяющий центр не соответствует '
                        'Gazprom Neft Intermediate CA')
            return False
        if cert_expiration_date < server_date:
            Logger.info('Срок действия сертификата истек')
            return False
        return True

    @classmethod
    def execute_nmap_scan(cls, ports: str, url: str) -> str:
        option = cls.PORTS_FLAG_CMD.format(ports=ports)
        nmap_cmd = cls.NMAP_SCAN_CMD.format(option=option, url=url)
        Logger.info(nmap_cmd)
        result = (subprocess.Popen(nmap_cmd, shell=True,
                                   stdout=subprocess.PIPE)).communicate()
        return result[0].decode('utf-8')

    @classmethod
    def execute_nmap_script_scan(cls, ports: str, script: str, url: str) -> str:
        option = ' '.join([cls.PORTS_FLAG_CMD.format(ports=ports),
                           cls.SCRIPT_FLAG_CMD.format(script=script)])
        nmap_cmd = cls.NMAP_SCAN_CMD.format(option=option, url=url)
        result = (subprocess.Popen(nmap_cmd, shell=True,
                                   stdout=subprocess.PIPE)).communicate()
        return result[0].decode('utf-8')

    @classmethod
    def __get_cert_date(cls, result: str) -> datetime:
        result_for_date = result.split("\n")
        cert_expiration_date = None
        for elem in result_for_date:
            if 'Not valid after' in elem:
                cert_expiration_date = elem
        cert_expiration_date = cert_expiration_date.split('  ')
        cert_expiration_date = cert_expiration_date[1].split('T')
        cert_expiration_date = cert_expiration_date[0].split('-')
        cert_expiration_date = datetime(int(cert_expiration_date[0]),
                                        int(cert_expiration_date[1]),
                                        int(cert_expiration_date[2]))
        return cert_expiration_date
