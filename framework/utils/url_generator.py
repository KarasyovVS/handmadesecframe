from framework.utils.logger import Logger


class URLGenerator:
    
    @staticmethod
    def switch_https_to_http(url):
        Logger.info("Замена схемы https на http в URL")
        return url.replace("https", "http")
    
    @staticmethod
    def url_contains_https(url):
        Logger.info("Проверка схемы https в URL")
        return "https" in url

    @staticmethod
    def generate_url_for_basic_auth(url, login, password):
        Logger.info("Генерация URL базовой аутентификации")
        url = url.split("://")
        url = url[0] + "://" + login + ":" + password + "@" + url[1]
        return url
