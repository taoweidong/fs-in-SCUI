from django.http import JsonResponse
# Create your views here.
from rest_framework import viewsets

from .models import Book, APIStatistics
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def article_detail(request):
    data = APIStatistics.objects.all()
    # 返回访问数量
    return JsonResponse({'data': list(data.values())})
