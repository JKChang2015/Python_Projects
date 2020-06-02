# -*- coding: UTF-8 -*-
# File name: a
# Created by JKChang
# 01/06/2020, 22:00
# Tag:
# Description: 处理请求和响应，我们很少去动它。

"""
WSGI config for myweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')

application = get_wsgi_application()
