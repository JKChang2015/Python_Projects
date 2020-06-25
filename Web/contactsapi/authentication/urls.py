# -*- coding: UTF-8 -*-
# File name: urls
# Created by JKChang
# 22/06/2020, 21:25
# Tag:
# Description: 

from django.contrib import admin
from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('register', RegisterView.as_view()),
]