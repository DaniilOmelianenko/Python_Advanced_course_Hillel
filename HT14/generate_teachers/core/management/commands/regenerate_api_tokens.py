from core.models import Teacher

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help_command = '''
    Regenerate API keys for all users
    command: regenerate_api_tokens
    '''

    def handle(self, *args, **kwargs):
        for user in Teacher.objects.all():
            call_command('drf_create_token', '-r', user.username)
