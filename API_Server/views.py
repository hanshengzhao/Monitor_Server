from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Server
from serializers import ServerSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def server_list(request):
    """
    List all server, or create a new task.
    """
    if request.method == 'GET':
        servers = Server.objects.all()
        serializer = ServerSerializer(servers,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServerSerializer(data=request.data)
        print dir(serializer)
        print serializer.fields
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def server_detail(request, name):
    """
    Get, udpate, or delete a specific task
    """
    try:
        server = Server.objects.get(server_name=name)
    except Server.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServerSerializer(server)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServerSerializer(server, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Server.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)