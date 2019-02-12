# -*- coding:utf-8 -*-
import datetime
from celery import schedules


BROKER_URL = "redis://localhost:6379/1"

CELERY_RESULT_BACKEND = "redis://localhost:6379/2"

CELERY_TIMEZONE = "Asia/Shanghai"  # 默认UTC

# 导入指定的任务模块
CELERY_IMPORTS = (
    "celery_app.task1",
    "celery_app.task2",
)

# 添加定时任务
CELERYBEAT_SCHEDULE = {
    "task1": {
        "task": "celery_app.task1.add",  # 将任务(task1)每10s执行一次
        "schedule": datetime.timedelta(seconds=10),  # 设置10s的过期时间
        "args": (2, 8)  # 添加task1任务的参数
    },
    "task2": {  # 每天的14:32执行task2
        "task": "celery_app.task2.multiply",
        "schedule": schedules.crontab(hour=14, minute=49),
        "args": (2, 3)
    }
}


# Worker: celery -A celery_app worker -l --loglevel=info
# Beat: celery -A celery_app beat --loglevel=info
# 一条命令启动Worker与Beat: celery -B -A celery_app worker --loglevel=info























