# result.py
import json

from django.http import JsonResponse

# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @Desc: { 项目信息返回结果模块 }
# @Date: 2021/09/23 22:10
from .enums import StatusCodeEnum


class R(object):
    """
    统一项目信息返回结果类
    """

    def __init__(self):
        self.code = None
        self.message = None
        self.data = dict()

    @staticmethod
    def table_data(total: int, page: int, page_size: int, rows: list):
        result = {
            'total': total,
            'page': page,
            'rows': rows,
            'pageSize': page_size,
        }
        table_result = {
            'code': StatusCodeEnum.OK.code,
            'data': result,
            'message': StatusCodeEnum.OK.errmsg,
        }
        return JsonResponse(data=table_result, safe=False)

    @staticmethod
    def success(code=StatusCodeEnum.OK.code, data=None, message=StatusCodeEnum.OK.errmsg):
        result = {
            'code': code,
            'data': data,
            'message': message,
        }
        return JsonResponse(data=result, safe=False)

    @staticmethod
    def ok(data=None):
        """
        组织成功响应信息
        :return:
        """
        r = R()
        r.code = StatusCodeEnum.OK.code
        r.message = StatusCodeEnum.OK.errmsg
        r.data = data
        return JsonResponse(data=r.__dict__, safe=False)


    @staticmethod
    def error(data=None):
        """
        组织错误响应信息
        :return:
        """
        r = R()
        r.code = StatusCodeEnum.ERROR.code
        r.message = StatusCodeEnum.ERROR.errmsg
        r.data = data
        return JsonResponse(data=r.__dict__, safe=False)

    @staticmethod
    def server_error(message='服务器异常'):
        """
        组织服务器错误信息
        :return:
        """
        r = R()
        r.code = StatusCodeEnum.SERVER_ERR.code
        r.message = message
        return JsonResponse(data=r.__dict__, safe=False)

    @staticmethod
    def set_result(enum):
        """
        组织对应枚举类的响应信息
        :param enum: 状态枚举类
        :return:
        """
        r = R()
        r.code = enum.code
        r.message = enum.message
        return r
