from django.shortcuts import render
import re
import time
import paramiko
import os
import logging
import json
import base64
import csv
import sys
from datetime import datetime
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, Http404, StreamingHttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.core.cache import cache

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.authtoken.models import Token
from .models import User
from .models import DeviceManage
import paramiko

logger = logging.getLogger(__name__)
# Create your views here.

class Login(APIView):
    @staticmethod
    def get(request):
        return render(request, 'login.html')
    @staticmethod
    def post(request):
        msg = {'info': ''}
        data = request.data
        user = data['username']
        pd = data['password']
        user_check = User.objects.filter(username=user, password=pd)
        if user_check:
            # request.session['username'] = user
            msg['info'] = 'ok'
            return HttpResponse(json.dumps(msg))
        msg['info'] = '用户名或密码错误'
        return HttpResponse(json.dumps(msg))

# class Home(APIView):
#     @staticmethod
#     def get(request):
#         return render(request, 'home.html')
#     @staticmethod
#     def post(request):
#         msg = {'result':'','status':''}
#         try:
#             data = request.data
#             l2tpuser = data['username']
#             l2tppasswd = data['password']
#             ssh = paramiko.SSHClient()
#             ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#             # ssh.connect(hostname='223.167.134.180', port=18730,
#             #             username='zhaoping', password='KingJuniper',
#             #             look_for_keys=False)
#             ssh.connect(hostname='222.72.130.58', port=22,
#                         username='useradmin', password='lianchi',
#                         look_for_keys=False)
#             command = '/ppp secret add name={} password={} service= any profile=default'.format(l2tpuser,l2tppasswd)
#             _, stdout, _ = ssh.exec_command(command)
#             ssh.close()
#         except Exception as err:
#             msg['result'] = err
#             msg['status'] = 0
#             return HttpResponse(json.dumps(msg))
#         msg['result'] = 'Success create user:{} and password:{}'.format(l2tpuser,l2tppasswd)
#         msg['status'] = 1
#         return HttpResponse(json.dumps(msg))

class Device(APIView):

    @staticmethod
    def get(request):
        data = DeviceManage.objects.all()
        return render(request, 'device.html', {'list': data})

    @staticmethod
    def post(request):
        msg = {'result':'','status':''}
        try:
            data = request.data
            rosuser = data['loginuser']
            rospasswd = data['loginpasswd']
            l2tpuser = data['l2tpuser']
            l2tppasswd = data['l2tppasswd']
            rosip = data['rosip']
            print(l2tpuser)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=rosip, port=18730,
                        username=rosuser, password=rospasswd,
                        look_for_keys=False)
            command = '/ppp secret add name={} password={} service= any profile=default'.format(l2tpuser,l2tppasswd)
            _, stdout, _ = ssh.exec_command(command)
            ssh.close()
        except Exception as err:
            print(err)
            # msg['result'] = err
            # msg['status'] = 0
            msg['result'] = 'EEE'
            msg['status'] = 0
            return HttpResponse(json.dumps(msg))
        msg['result'] = 'Success create user:{} and password:{}'.format(l2tpuser,l2tppasswd)
        msg['status'] = 1
        return HttpResponse(json.dumps(msg))