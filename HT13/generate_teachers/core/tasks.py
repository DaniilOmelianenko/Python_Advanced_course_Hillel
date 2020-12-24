# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from datetime import date, timedelta

from core.models import Logger
from core.models import Teacher
from core.rates import get_kurstoday_rate, get_minfin_mejbank_rate,\
    get_mono_rate, get_national_bank_rate, get_vkurse_rate

from django.core.mail import send_mail
from django.core.management import call_command

from generate_teachers import celery_app


@celery_app.task
def send_mail_task(title, message, email):
    send_mail(
        subject=title,
        message=message,
        recipient_list=['support@support.com'],
        from_email=email
    )


@celery_app.task
def delete_old_logs():
    old_date = date.today() - timedelta(days=7)
    Logger.objects.filter(creation_date__lte=old_date).delete()


#  ---------- PARSE CURRENCY ---------------------
@celery_app.task
def collect_currency_rates():
    get_vkurse_rate()
    get_mono_rate()
    get_minfin_mejbank_rate()
    get_national_bank_rate()
    get_kurstoday_rate()


#  ---------- UPDATE API KEYS ---------------------
# @celery_app.task
# def generate_new_api_token():
#     for user in Teacher.objects.all():
#         Token.objects.update(user=user, key=Token.generate_key())
#         Token.generate_key()


@celery_app.task
def generate_new_api_token():
    for user in Teacher.objects.all():
        call_command('drf_create_token', '-r', user.username)
