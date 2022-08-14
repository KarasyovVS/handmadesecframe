import json

from framework.utils.logger import Logger


class JSONManager:

    @staticmethod
    def get_data(file):
        try:
            with open(file) as data_file:
                data_dict = json.load(data_file)
                return data_dict
        except FileNotFoundError:
            Logger.error("File not found")
            raise FileNotFoundError
