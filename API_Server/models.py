# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Server(models.Model):
    server_name = models.CharField(max_length=48)
    server_ID = models.CharField(max_length=128,unique=True)
    server_status = models.CharField(max_length=128)
    server_interval = models.CharField(max_length=128)

    class Meta:
        verbose_name = '注册服务'
        verbose_name_plural = '注册服务'

    def __unicode__(self):
        return  self.server_name


class Server_monitor(models.Model):

    class Meta:
        verbose_name = '服务监控提交'
        verbose_name_plural = '服务监控提交'