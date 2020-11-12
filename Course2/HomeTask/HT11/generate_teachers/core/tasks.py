from datetime import date, timedelta

from core.models import Logger

from django.core.mail import send_mail

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


# @celery_app.task
# def delete_old_logs():
#     old_date = date.today() - timedelta(minutes=5)
#     Logger.objects.filter(creation_date__lte=old_date).delete()
