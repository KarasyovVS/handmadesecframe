from framework.utils.logger import Logger


class URLGenerator:
    
    @staticmethod
    def switch_https_to_http(url):
        Logger.info("Меняем схему https на http в URL")
        return url.replace("https", "http")
    
    @staticmethod
    def prepare_url_for_sslyze(url):
        Logger.info("Подготовка URL для sslyze")
        return (url.split("://"))[1]

    # @staticmethod
    # def generate_url_for_basic_auth(url, login, password):
    #     Logger.info("Generating URL for basic authorization")
    #     url = url.split("://")
    #     url = url[0] + "://" + login + ":" + password + "@" + url[1]
    #     return url
