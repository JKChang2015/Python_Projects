# -*- coding: UTF-8 -*-
# File name: a
# Created by JKChang
# 01/06/2020, 22:06
# Tag:
# Description: 用于管理应用本身的文件，包括应用的名字如何命名，默认就是 learn 。

from django.apps import AppConfig


class LearnConfig(AppConfig):
    name = 'learn'
