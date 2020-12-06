# Generated by Django 3.1.2 on 2020-12-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_currency_currency_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='bank',
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, 'NATIONAL_BANK'),
                    (2, 'MINFIN_MEJBANK'),
                    (3, 'VKURSE_DP'),
                    (4, 'MONO'),
                    (5, 'KURSTODAY')
                ]
            ),
        ),
    ]