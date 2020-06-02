# -*- coding: UTF-8 -*-
# File name: manage
# Created by JKChang
# 01/06/2020, 22:00
# Tag:
# Description: 项目的入口文件，在后面的实验中我们会大量使用它来执行一些命令用来创建应用、启动项目、控制数据表迁移等。

# !/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
