from framework.utils.json_manager import JSONManager
from framework.singleton import Singleton


class DataClass(metaclass=Singleton):

    def __init__(self):
        self.__DATA_DICT = JSONManager.get_data("tests/data.json")

    @classmethod
    def get_attr(cls, attr):
        return cls().__DATA_DICT[attr]
