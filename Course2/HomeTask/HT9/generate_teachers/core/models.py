# from core.fields import PhoneField
# from core.signals import notify
# from django.db.models.signals import post_save, pre_save
from django.db import models
from django.db.models.signals import pre_save

from phone_field import PhoneField


class Teacher(models.Model):
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
    # phone = PhoneField(
    #     null=False,
    #     default=""
    # )

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

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
        Teacher,
        on_delete=models.CASCADE,
        verbose_name="Учитель"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Student(models.Model):
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
    # phone = PhoneField(
    #     null=True,
    #     blank=True
    # )
    phone = PhoneField(
        blank=True,
        help_text='Contact phone number'
    )

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.age}'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


# def send_notify(**kwargs):
#     notify('Base was updated!')


def change_name(instance, **kwargs):
    instance.firstname = instance.firstname.capitalize()
    instance.lastname = instance.lastname.capitalize()


# post_save.connect(send_notify, sender=Student)
# post_save.connect(send_notify, sender=Teacher)
pre_save.connect(change_name, sender=Student)
pre_save.connect(change_name, sender=Teacher)


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
