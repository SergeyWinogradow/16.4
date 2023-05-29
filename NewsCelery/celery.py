import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '9-2-main.settings')

app = Celery('NewsCelery')
app.config_from_object('django.conf:settings', namespace='CELERY')

# переодические задачи
app.conf.beat_schedule = {
    # имя задачи произвольное
    'mail_send':{
        # таск прописываем путь
        'task': 'news.tasks.send_mail',
        'schedule': crontab(minute='*/1'),# запускаем каждую минуту
    }
}

app.autodiscover_tasks()# самостоятельно ищет всевозможные таски