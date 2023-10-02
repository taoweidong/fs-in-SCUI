# Create your models here.
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    class Meta:
        db_table = 'tb_book'
        verbose_name = "访问记录表"
        verbose_name_plural = verbose_name

class APIStatistics(models.Model):
    api_name = models.CharField(max_length=255)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.api_name

    class Meta:
        db_table = 'sys_visit'
        verbose_name = "访问记录表"
        verbose_name_plural = verbose_name
