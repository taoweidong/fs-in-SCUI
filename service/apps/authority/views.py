from django.core import serializers
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from apps.authority.models import OpLogs
from utils.result import R


def token(request):
    response = {
        "code": 200,
        "data": {
            "token": "SCUI.Administrator.Auth",
            "userInfo": {
                "userId": "1",
                "userName": "Administrator",
                "dashboard": "0",
                "role": [
                    "SA",
                    "admin",
                    "Auditor"
                ]
            }
        },
        "message": ""
    }
    return JsonResponse(response)


def operation_list(request):
    page_number = int(request.GET.get('page'))
    records_per_page = int(request.GET.get('pageSize'))
    queryset = OpLogs.objects.all()
    paginator = Paginator(queryset, records_per_page)  # 每页显示指定数量的记录
    page_obj = paginator.get_page(page_number)  # 获取指定页码的对象
    total = paginator.count
    json_data = []
    for i in page_obj.object_list:
        json_data.append(model_to_dict(i))
    data = R.table_data(page=page_number, page_size=records_per_page, total=total, rows=json_data)
    return JsonResponse(data=data, safe=False)
