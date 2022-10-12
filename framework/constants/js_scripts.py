class JSScripts(object):

    GET_LOCAL_STORAGE_LEN = "return window.localStorage.length;"
    GET_ALL_ITEMS =         "var ls = window.localStorage, items = {}; " \
                            "for (var i = 0, k; i < ls.length; ++i) " \
                            "  items[k = ls.key(i)] = ls.getItem(k); " \
                            "return items; "
    GET_ALL_KEYS =          "var ls = window.localStorage, keys = []; " \
                            "for (var i = 0; i < ls.length; ++i) " \
                            "  keys[i] = ls.key(i); " \
                            "return keys; "
    GET_ITEM =              "return window.localStorage.getItem(arguments[0]);"
    SET_ITEM =              "window.localStorage.setItem(arguments[0], " \
                            "arguments[1]);"
    CLEAR_STORAGE =         "window.localStorage.clear();"
    REMOVE_ITEM =           "window.localStorage.removeItem(arguments[0]);"
    