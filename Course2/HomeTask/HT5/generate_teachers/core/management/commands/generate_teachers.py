from django.core.management.base import BaseCommand
from core.models import Teacher
import names
from random import randint


class Command(BaseCommand):
    help = 'Generate 100 random teachers'

    def handle(self, *args, **kwargs):
        for i in range(100):
            name = names.get_first_name()
            lastname = names.get_last_name()
            age = int(randint(21, 85))
            teacher = Teacher(firstname=name, lastname=lastname, age=age)
            teacher.save()
