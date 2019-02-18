# -*- coding:utf-8 -*-
# !/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imooc.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

"""
在Django中使用celery
Install: pip install django-celery
项目启动: python manage.py runserver
Worker: python manage.py celery worker --loglevel=info

监控工具
Install: pip install flower==0.9.0
Start: celery flower --address=0.0.0.0 --port=5555 --broker=xxx --basic_auth=imooc:imooc
或者使用 python manage.py celery flower # 从manage.py配置文件中读取配置信息
"""
