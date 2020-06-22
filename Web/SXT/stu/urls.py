# -*- coding: UTF-8 -*-
# File name: urls
# Created by JKChang
# 19/06/2020, 16:39
# Tag:
# Description: 

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view),
    path('login/',views.login_view)
]
