from django.db import models

# Create your models here.
class c_data(models.Model):
    people = models.CharField(verbose_name='人数', max_length=1024, null=True, blank=True)
    title = models.TextField(verbose_name='课题', max_length=64, null=True, blank=True)
    url = models.CharField(verbose_name='课程链接', max_length=128, null=True, blank=True)
    mark = models.FloatField(verbose_name='评分', null=True, blank=True)
    text_data = models.TextField(verbose_name='课程内容', max_length=10000, null=True, blank=True)