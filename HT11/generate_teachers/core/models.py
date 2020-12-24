# from core.fields import PhoneField
# from core.signals import notify
# from django.db.models.signals import post_save, pre_save
# from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save

from phone_field import PhoneField


class Teacher(AbstractUser):
    # firstname = models.CharField(
    #     max_length=255,
    #     null=False,
    #     default="",
    #     verbose_name="Имя"
    # )
    # lastname = models.CharField(
    #     max_length=255,
    #     null=False,
    #     default="",
    #     verbose_name="Фамилия"
    # )
    age = models.IntegerField(
        null=False,
        default=1,
        verbose_name="Возраст"
    )

    # phone = PhoneField(
    #     null=False,
    #     default=""
    # )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # def save(self, **kwargs):
    #     # pre save
    #     resp = super(Teacher, self).save(**kwargs)    # вмессто сигналов
    #     # post save
    #     return resp

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


class Group(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    teacher = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Учитель",
        related_name="teacher_groups"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Student(models.Model):
    EXPERIENCE_TRAINEE = 0
    EXPERIENCE_JUNIOR = 1
    EXPERIENCE_MIDDLE = 2
    EXPERIENCE_SENIOR = 3

    EXPERIENCE_CHOICES = (
        (EXPERIENCE_TRAINEE, 'TRAINEE'),
        (EXPERIENCE_JUNIOR, 'JUNIOR'),
        (EXPERIENCE_MIDDLE, 'MIDDLE'),
        (EXPERIENCE_SENIOR, 'SENIOR')
    )

    firstname = models.CharField(
        max_length=255,
        null=False,
        default="",
        verbose_name="Имя"
    )
    lastname = models.CharField(
        max_length=255,
        null=False,
        default="",
        verbose_name="Фамилия"
    )
    age = models.IntegerField(
        null=False,
        default=1,
        verbose_name="Возраст"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET("Without Group"),
        verbose_name="Группа",
        related_name='students'
    )
    # group = models.ManyToManyField(
    #     Group,
    #     blank=True,
    #     verbose_name="Группа"
    # )
    phone = PhoneField(
        blank=True,
        help_text='Contact phone number'
    )
    experience = models.PositiveSmallIntegerField(
        choices=EXPERIENCE_CHOICES,
        default=0
    )

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.age}'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


# def send_notify(**kwargs):
#     notify('Base was updated!')


def change_name_teacher(instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()


def change_name_student(instance, **kwargs):
    instance.firstname = instance.firstname.capitalize()
    instance.lastname = instance.lastname.capitalize()


# post_save.connect(send_notify, sender=Student)
# post_save.connect(send_notify, sender=Teacher)
pre_save.connect(change_name_student, sender=Student)
pre_save.connect(change_name_teacher, sender=Teacher)


class Logger(models.Model):
    path = models.CharField(
        max_length=255,
        null=False,
        default=""
    )

    method = models.CharField(
        max_length=255,
        null=False,
        default=""
    )

    execution_time = models.CharField(
        max_length=255,
        null=False,
        default=""
    )

    creation_date = models.DateField(
        auto_now_add=True
    )


class Currency(models.Model):
    CURRENCY_USD = 1
    CURRENCY_EUR = 2
    CURRENCY_RUR = 3

    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_EUR, 'EUR'),
        (CURRENCY_RUR, 'RUR')
    )
    currency_name = models.PositiveSmallIntegerField(choices=CURRENCY_CHOICES)
    currency_code = models.PositiveSmallIntegerField()
    currency_buy_rate = models.DecimalField(max_digits=10, decimal_places=2)
    currency_sell_rate = models.DecimalField(max_digits=10, decimal_places=2)
    currency_rate_date = models.DateTimeField(auto_now_add=True)
    bank = models.CharField(max_length=30)
