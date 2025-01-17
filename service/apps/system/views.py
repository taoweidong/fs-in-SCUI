import json
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import JsonResponse
from django.utils.timezone import now

from apps.system.models import OpLogs, Dictionary
from utils.result import R

logger = logging.getLogger(__name__)


# Create your views here.
def hello(request):
    logger.info("触发查询")
    return JsonResponse(data="hello")


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
    return R.table_data(page=page_number, page_size=records_per_page, total=total, rows=json_data)


def dict_list(request):
    page_number = int(request.GET.get('page'))
    records_per_page = int(request.GET.get('pageSize'))
    code = str(request.GET.get('code')).strip()

    dict_info = Dictionary.objects.filter(code=code).first()
    if dict_info is None:
        data = R.table_data(page=page_number, page_size=records_per_page, total=0, rows=[])
        return JsonResponse(data=data, safe=False)
    queryset = Dictionary.objects.filter(parent_id=dict_info.id).order_by('sort').all()
    paginator = Paginator(queryset, records_per_page)  # 每页显示指定数量的记录
    page_obj = paginator.get_page(page_number)  # 获取指定页码的对象
    total = paginator.count
    json_data = []
    for i in page_obj.object_list:
        json_data.append(model_to_dict(i))
    return R.table_data(page=page_number, page_size=records_per_page, total=total, rows=json_data)


def dict_tree(request):
    queryset = Dictionary.objects.filter(parent_id=None).all()
    json_data = []
    for i in queryset:
        json_data.append(model_to_dict(i))
    return R.success(data=json_data)


def dict_save(request):
    param = json.loads(request.body)
    dict_id = param.get('id', '')
    name = param.get('name')
    code = param.get('code')
    sort = param.get('sort', 1)

    if dict_id is None or len(str(dict_id).strip()) == 0:
        # 新增
        new_dict = Dictionary(code=code, name=name, update_datetime=now(), sort=int(sort))
        new_dict.save()
    else:
        dict_data = Dictionary.objects.filter(id=dict_id).get()
        dict_data.code = code
        dict_data.name = name
        dict_data.update_datetime = now()
        dict_data.sort = sort
        dict_data.save()

    return R.success()


def save_sub(request):
    param = json.loads(request.body)
    dict_sub_id = param.get('id', '')
    dict_id = param.get('dic', '')
    code = param.get('code')
    name = param.get('name')
    status = param.get('status')
    sort = int(param.get('sort'))

    if dict_sub_id is None or len(str(dict_sub_id).strip()) == 0:
        # 新增
        new_dict = Dictionary(code=code, name=name, create_datetime=now(), status=status, parent_id=dict_id, sort=sort)
        new_dict.save()
    else:
        dict_data = Dictionary.objects.filter(id=dict_sub_id).get()
        dict_data.parent_id = dict_id
        dict_data.code = code
        dict_data.name = name
        dict_data.status = status
        dict_data.update_datetime = now()
        dict_data.sort = sort
        dict_data.save()

    return R.success()


def delete(request):
    param = json.loads(request.body)
    dict_ids = param.get('id', [])
    Dictionary.objects.filter(parent_id__in=dict_ids).delete()
    Dictionary.objects.filter(id__in=dict_ids).delete()
    return R.success(data="删除成功")


def refresh_status(request):
    param = json.loads(request.body)
    dict_id = param.get('id', '')
    status = param.get('value', True)

    try:
        dict_data = Dictionary.objects.filter(id=dict_id).get()
        # 查询成功，执行相应的操作
        dict_data.status = status
        dict_data.update_datetime = now()
        dict_data.save()
        return R.success(data="状态更新成功")
    except ObjectDoesNotExist:
        # 查询结果不存在，执行相应的操作
        logger.exception(f"对象不存在:{dict_id}")

    return R.success(data=f"对象不存在:{dict_id}")


def dict_get(request):
    code = request.GET.get('code')
    dict_info = Dictionary.objects.filter(code=code).first()
    result = []
    if dict_info is None:
        return JsonResponse(data=R.success(data=result), safe=False)
    queryset = Dictionary.objects.filter(parent_id=dict_info.id).all()
    json_data = []
    for i in queryset:
        if i.status:
            json_data.append({"key": i.code, "label": i.name})
    return R.success(data=json_data)
