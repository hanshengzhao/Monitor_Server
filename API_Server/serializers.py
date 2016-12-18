# coding:utf-8
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from models import Server

from rest_framework import serializers


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('server_name', 'server_ID', 'server_status')
