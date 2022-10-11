from abc import ABC


class BaseModel(ABC):

    def __init__(self, **kwargs):
        for elem in kwargs:
            setattr(self, elem, kwargs[elem])

    def __eq__(self, other):
        flag = True
        dir_list = [elem for elem in dir(self)
                    if elem not in dir(self.__class__)]
        for attr in dir_list:
            if getattr(other, attr) != getattr(self, attr):
                flag = False
        return flag

    def del_attr(self, attr):
        delattr(self, attr)

    def model_is_not_empty(self):
        return len(dir(self)) - len(dir(self.__class__)) > 0
