import logging

from django.utils.deprecation import MiddlewareMixin

from apps.api.models import APIStatistics

logger = logging.getLogger(__name__)


class RequestCountMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.get_response = get_response

    def process_request(self, request):
        logger.debug('This is a debug message  测试日志')
        logger.info('This is an info message  测试日志')
        logger.warning('This is a warning message  测试日志')
        logger.error('This is an error message  测试日志')
        # 在请求到达视图函数前进行处理
        # 这里可以增加一些条件判断，例如只统计特定的接口
        # 在每个请求上增加一个访问计数属性
        request.visit_count = 0
        # 可以将统计信息保存在数据库中
        api_name = request.path_info  # 以接口路径作为唯一标识
        statistics, created = APIStatistics.objects.get_or_create(api_name=api_name)
        statistics.visit_count += 1
        statistics.save()

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 在视图函数被调用前进行处理
        # 增加访问计数
        request.visit_count += 1

    def process_response(self, request, response):
        # 在响应返回给客户端前进行处理
        # 可以在此处对统计结果进行进一步处理
        return response
