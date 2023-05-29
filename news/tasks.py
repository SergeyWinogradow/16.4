from celery import shared_task
from django.core.mail import send_mail

# отправка почты
@shared_task
def send_m():
    send_mail(
        'Subject here',#заголовок
        'Here is the message.',#сообщение
        'poc47a.t@yandex.ru',#откуда отправляем
        ['to@yandex.ru'],#кому отправляем
        fail_silently=False,
    )
