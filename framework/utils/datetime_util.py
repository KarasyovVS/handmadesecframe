# coding=utf-8
from datetime import datetime, timezone


class DatetimeUtil(object):
    @staticmethod
    def get_str_datetime(exp_format):
        return datetime.now().strftime(exp_format)
