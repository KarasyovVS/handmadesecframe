import requests

# from framework.constants.status_codes import StatusCodes
from framework.utils.logger import Logger
from tests.config.urls import Urls


class APIUtils:

    def __init__(self, url=Urls.TEST_STAND_URL, path=None,
                 method=None, params=None):
        if path is None:
            if method is not None:
                self.__URL = url.format(METHOD=method, PARAMS=params,
                                        TOKEN=None,
                                        V=None)
            else:
                self.__URL = url
        else:
            self.__URL = url + path

    def send_post_request(self, data=None, files=None):
        Logger.info("Sending post request to URL '" + self.__URL + "'")
        self.RESPONSE = requests.post(self.__URL, data=data, files=files)

    def send_get_request(self):
        Logger.info("Sending get request to URL '" + self.__URL)
        self.RESPONSE = requests.get(self.__URL)

    def get_info_from_json(self):
        Logger.info("Getting info from the JSON response")
        return self.RESPONSE.json()

    def get_status_code(self):
        Logger.info("Getting status code from the response")
        return self.RESPONSE.status_code

    def check_status_code(self, status_code=StatusCodes.OK):
        return self.get_status_code() == status_code

    def get_text(self):
        Logger.info("Getting text from the response")
        return self.RESPONSE.text

    def get_content(self):
        Logger.info("Getting content from the response")
        return self.RESPONSE.content

    def get_headers(self):
        Logger.info("Getting headers from the response")
        return self.RESPONSE.headers
