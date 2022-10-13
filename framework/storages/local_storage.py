from framework.constants.js_scripts import JSScripts
from framework.browser.browser import Browser


class LocalStorage(object):
    
    def __init__(self):
        self.driver = Browser()

    def __len__(self):
        return self.driver.execute_script(JSScripts.GET_LOCAL_STORAGE_LEN)

    def items(self) :
        return self.driver.execute_script(JSScripts.GET_ALL_ITEMS)

    def keys(self) :
        return self.driver.execute_script(JSScripts.GET_ALL_KEYS)

    # def get(self, key):
    #     return self.driver.execute_script(JSScripts.GET_ITEM, key)

    # def set(self, key, value):
    #     self.driver.execute_script(JSScripts.SET_ITEM, [key, value])

    # def has(self, key):
    #     return key in self.keys()

    # def remove(self, key):
    #     self.driver.execute_script(JSScripts.REMOVE_ITEM, key)

    def clear(self):
        self.driver.execute_script(JSScripts.CLEAR_STORAGE)

    def __getitem__(self, key) :
        value = self.get(key)
        if value is None :
          raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        return self.items().__iter__()

    def __repr__(self):
        return self.items().__str__()