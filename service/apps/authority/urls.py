from django.urls import path

from . import views

urlpatterns = [
    path('token', views.token, name='token'),
    path('operation', views.operation_list, name='operation'),
]
