from core.rates import get_kurstoday_rate, get_minfin_mejbank_rate,\
    get_mono_rate, get_national_bank_rate, get_vkurse_rate

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help_command = 'Take Currency'

    def handle(self, *args, **kwargs):
        get_vkurse_rate()
        get_mono_rate()
        get_minfin_mejbank_rate()
        get_national_bank_rate()
        get_kurstoday_rate()
