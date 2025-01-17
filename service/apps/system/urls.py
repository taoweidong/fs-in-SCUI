from django.urls import path

from apps.system import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('operation', views.operation_list, name='operation'),
    path('dic/get', views.dict_get, name='dict_get'),
    path('dic/tree', views.dict_tree, name='dict_tree'),
    path('dic/list', views.dict_list, name='dict_list'),
    path('dic/save', views.dict_save, name='dict_save'),
    path('dic/delete', views.delete, name='dict_delete'),
    path('dic/save_sub', views.save_sub, name='save_sub'),
    path('dic/refresh_status', views.refresh_status, name='refresh_status'),
]
