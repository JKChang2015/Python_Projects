# -*- coding: UTF-8 -*-
# File name: a
# Created by JKChang
# 01/06/2020, 22:06
# Tag:
# Description: 创建视图函数的文件，视图函数用于处理客户端发来的请求。

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Greeting from Jiakang')
