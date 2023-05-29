from logging import DEBUG
from logging.handlers import RotatingFileHandler
import logging.handlers
import sys


# корневой регистратор
logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# логгеры для определенных модулей
django_logger = logging.getLogger('django')
django_request_logger = logging.getLogger('django.request')
django_server_logger = logging.getLogger('django.server')
django_template_logger = logging.getLogger('django.template')
django_db_logger = logging.getLogger('django.db.backends')
django_security_logger = logging.getLogger('django.security')

# обработчик консоли для уровня DEBUG и выше
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
console_handler.addFilter(logging.Filter() if DEBUG else logging.Filter(True))

#  обработчик файла для general.log
general_log_handler = RotatingFileHandler('general.log', maxBytes=1000000, backupCount=5)
general_log_handler.setLevel(logging.INFO)
general_log_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] [%(module)s] %(message)s'))

# обработчик файла для errors.log
errors_log_handler = RotatingFileHandler('errors.log', maxBytes=1000000, backupCount=5)
errors_log_handler.setLevel(logging.ERROR)
errors_log_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] [%(module)s] %(message)s\n%(pathname)s\n%(exc_info)s'))

# обработчик файла для security.log
security_log_handler = RotatingFileHandler('security.log', maxBytes=1000000, backupCount=5)
security_log_handler.setLevel(logging.INFO)
security_log_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] [%(module)s] %(message)s'))

# почтовый обработчик для уровня ERROR и выше
mail_handler = logging.handlers.SMTPHandler(
    mailhost=("smtp.yandex.ru", 465),
    fromaddr="poc47a.t@yandex.ru",
    toaddrs=["subscriber.email"],
    subject="[ERROR] Application Error"
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s\n%(pathname)s'))

# обработчики и фильтры к регистраторам
root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.addHandler(general_log_handler)
root_logger.addHandler(errors_log_handler)
root_logger.addHandler(security_log_handler)
root_logger.addHandler(mail_handler)

django_logger.addHandler(console_handler)
django_logger.addHandler(general_log_handler)

django_request_logger.addHandler(errors_log_handler)
django_server_logger.addHandler(errors_log_handler)

django_request_logger.addHandler(mail_handler)
django_server_logger.addHandler(mail_handler)

django_logger.addHandler(security_log_handler)


logger = logging.getLogger(__name__)

def my_view(request):
    logger.debug('Это сообщение уровня DEBUG')
    logger.info('Это сообщение уровня INFO')
    logger.warning('Это сообщение уровня WARNING')
    logger.error('Это сообщение уровня ERROR')
    logger.critical('Это сообщение уровня CRITICAL')