from django.urls import path

from apps.system import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('operation', views.operation_list, name='operation'),
]
