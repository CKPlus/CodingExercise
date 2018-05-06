import calendar
import json
from datetime import datetime


class ClientResult(object):
    '''This class is for generate a general json response with status code'''

    def __init__(self):
        self.__status = {}
        self.__data = {}

    def status(self, code, message):
        self.__status = {'code': code, 'message': message}

    def data(self, data):
        self.__data = data

    def to_json(self, cvt_dt_to_int=False):

        if self.__status:
            return json.dumps(
                self.__status,
                separators=(',', ':'),
                default=self._json_handler(cvt_dt_to_int))

        return json.dumps(
            self.__data,
            separators=(',', ':'),
            default=self._json_handler(cvt_dt_to_int))

    def _json_handler(self, cvt_dt_to_int=False):
        def decorated(obj):
            if isinstance(obj, datetime):
                return int(calendar.timegm(obj.timetuple())) \
                    if cvt_dt_to_int else str(obj)
        return decorated
