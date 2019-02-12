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
"""
