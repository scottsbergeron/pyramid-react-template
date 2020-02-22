from abc import ABC
from datetime import datetime
from pyramid.response import Response


class BaseView(ABC):

    @staticmethod
    def json_response(json):
        """"
        :param dict | list json:
        :rtype: dict | list
        """
        if isinstance(json, dict):
            result = BaseView._dict_response(json)
        elif isinstance(json, list):
            result = BaseView._list_response(json)
        else:
            result = json
        return result

    @staticmethod
    def empty_response():
        """
        :rtype: Response
        """
        return Response(status=204)

    @staticmethod
    def options():
        """
        :rtype: Response
        """
        return BaseView.empty_response()

    @staticmethod
    def _dict_response(_dict):
        """"
        :param dict _dict:
        :rtype: dict
        """
        result = {}
        for key, value in _dict.items():
            if isinstance(value, dict):
                result[key] = BaseView._dict_response(value)
            elif isinstance(value, list):
                result[key] = BaseView._list_response(value)
            elif isinstance(value, datetime):
                result[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            else:
                result[key] = value
        return result

    @staticmethod
    def _list_response(_list):
        """"
        :param list _list:
        :rtype: list
        """
        result = []
        for value in _list:
            if isinstance(value, dict):
                result.append(BaseView._dict_response(value))
            elif isinstance(value, list):
                result.append(BaseView._list_response(value))
            elif isinstance(value, datetime):
                result.append(value.strftime('%Y-%m-%d %H:%M:%S'))
            else:
                result.append(value)
        return result

    def __init__(self, request):
        """
        :param pyramid.request.Request request:
        """
        self._request = request
