from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='API 接口文档')),
]
