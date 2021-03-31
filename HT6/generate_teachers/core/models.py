from django.db import models


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

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

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
        on_delete=models.SET("No Teacher"),
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

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.age}'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
