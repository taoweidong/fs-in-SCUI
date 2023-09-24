# result.py
import json

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
    def success(code=StatusCodeEnum.OK.code, data=None, message=StatusCodeEnum.OK.errmsg):
        result = {
            'code': code,
            'data': json.dumps(data),
            'message': message,
        }
        return result

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
        return r.__dict__

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
        return r

    @staticmethod
    def server_error(message='服务器异常'):
        """
        组织服务器错误信息
        :return:
        """
        r = R()
        r.code = StatusCodeEnum.SERVER_ERR.code
        r.message = message
        return r

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
