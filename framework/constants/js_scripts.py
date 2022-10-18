class JSScripts(object):

    GET_LS_LEN =            "return window.localStorage.length;"
    GET_ALL_LS_ITEMS =      "var ls = window.localStorage, items = {}; " \
                            "for (var i = 0, k; i < ls.length; ++i) " \
                            "  items[k = ls.key(i)] = ls.getItem(k); " \
                            "return items; "
    GET_ALL_LS_KEYS =       "var ls = window.localStorage, keys = []; " \
                            "for (var i = 0; i < ls.length; ++i) " \
                            "  keys[i] = ls.key(i); " \
                            "return keys; "
    GET_LS_ITEM =           "return window.localStorage.getItem(arguments[0]);"
    SET_LS_ITEM =           "window.localStorage.setItem(arguments[0], " \
                            "arguments[1]);"
    CLEAR_LS =              "window.localStorage.clear();"
    REMOVE_LS_ITEM =        "window.localStorage.removeItem(arguments[0]);"
    GET_PAGE_READY_STATE =  "return document.readyState"
    SCROLL_INTO_VIEW =      "arguments[0].scrollIntoView();"