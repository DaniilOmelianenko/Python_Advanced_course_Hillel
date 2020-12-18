import json

from core.models import Currency

from lxml import html

import requests

# from pprint import pprint


def get_national_bank_rate():
    response = requests.get(
        'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    )
    if response.status_code == 200:
        my_json_data = json.loads(response.content)
        bank = 'National Bank'
        found_currency_list = []

        def write_currency_list(currency_choice_name, currency_code):
            found_currency_list.append(Currency(
                currency_name=currency_choice_name,
                currency_code=currency_code,
                currency_buy_rate=currency_dict['rate'],
                currency_sell_rate=currency_dict['rate'],
                bank=bank
            ))

        for currency_dict in my_json_data:
            # print(currency_dict)
            if currency_dict['cc'] == 'USD':
                write_currency_list(1, 840)
            if currency_dict['cc'] == 'EUR':
                write_currency_list(2, 978)
            if currency_dict['cc'] == 'RUB':
                write_currency_list(3, 643)

        Currency.objects.bulk_create(found_currency_list)
    else:
        print(response.status_code)  # noqa


def get_minfin_mejbank_rate():
    response = requests.get('https://api.minfin.com.ua/mb/aa768465505925fa08f8c59bde39c810e6f0542f/') # noqa
    if response.status_code == 200:
        my_json_data = json.loads(response.content)
        bank = 'Minfin-Mejbank'
        found_currency_list = []

        def write_currency_list(currency_choice_name, currency_code):
            found_currency_list.append(Currency(
                currency_name=currency_choice_name,
                currency_code=currency_code,
                currency_buy_rate=currency_dict['bid'],
                currency_sell_rate=currency_dict['ask'],
                bank=bank
            ))

        for currency_dict in my_json_data:
            # print(currency_dict)
            if currency_dict['currency'] == 'usd':
                write_currency_list(1, 840)
            if currency_dict['currency'] == 'eur':
                write_currency_list(2, 978)
            if currency_dict['currency'] == 'rub':
                write_currency_list(3, 643)

        Currency.objects.bulk_create(found_currency_list)
    else:
        print(response.status_code)  # noqa


def get_vkurse_rate():
    response = requests.get('http://vkurse.dp.ua/course.json')
    if response.status_code == 200:
        my_json_data = json.loads(response.content)
        found_currency_list = []
        bank = 'Vkurse_dp'

        def write_currency_list(name, currency_choice_name, currency_code):
            found_currency_list.append(Currency(
                currency_name=currency_choice_name,
                currency_code=currency_code,
                currency_buy_rate=(my_json_data[name])['buy'],
                currency_sell_rate=(my_json_data[name])['sale'],
                bank=bank
            ))

        write_currency_list('Dollar', 1, 840)
        write_currency_list('Euro', 2, 978)
        write_currency_list('Rub', 3, 643)
        Currency.objects.bulk_create(found_currency_list)
    else:
        print(response.status_code)  # noqa


def get_mono_rate():
    response = requests.get('https://api.monobank.ua/bank/currency')
    if response.status_code == 200:
        my_json_data = json.loads(response.content)
        # my_json_data = response.json()  #  without requests
        bank = 'Mono'
        found_currency_list = []

        def write_currency_list(currency_choice_name):
            found_currency_list.append(Currency(
                currency_name=currency_choice_name,
                currency_code=currency_dict['currencyCodeA'],
                currency_buy_rate=currency_dict['rateBuy'],
                currency_sell_rate=currency_dict['rateSell'],
                bank=bank
            ))

        for currency_dict in my_json_data:
            if currency_dict['currencyCodeA'] == 840 and currency_dict['currencyCodeB'] == 980:  # noqa
                write_currency_list(1)
            if currency_dict['currencyCodeA'] == 978 and currency_dict['currencyCodeB'] == 980:  # noqa
                write_currency_list(2)
            if currency_dict['currencyCodeA'] == 643 and currency_dict['currencyCodeB'] == 980:  # noqa
                write_currency_list(3)
        Currency.objects.bulk_create(found_currency_list)
    else:
        print(response.status_code)  # noqa


def get_kurstoday_rate():
    response = requests.get('https://kurstoday.com.ua/')
    if response.status_code == 200:
        lxml_tree = html.fromstring(response.text)
        bank = 'Kurstoday'
        found_currency_list = []

        rate_date = [
            {
                'currency': 1,
                'code': 840,
                'buy': '//*[@id="aval"]/div/div[2]/table/tbody/tr[1]/td[2]/span[1]', # noqa
                'sell': '//*[@id="aval"]/div/div[2]/table/tbody/tr[1]/td[3]/span[1]' # noqa
            },
            {
                'currency': 2,
                'code': 978,
                'buy': '//*[@id="aval"]/div/div[2]/table/tbody/tr[2]/td[2]/span[1]', # noqa
                'sell': '//*[@id="aval"]/div/div[2]/table/tbody/tr[2]/td[3]/span[1]' # noqa
            },
            {
                'currency': 3,
                'code': 643,
                'buy': '//*[@id="aval"]/div/div[2]/table/tbody/tr[3]/td[2]/span[1]', # noqa
                'sell': '//*[@id="aval"]/div/div[2]/table/tbody/tr[3]/td[3]/span[1]' # noqa
            }
        ]

        for currency_dict in rate_date:
            found_currency_list.append(Currency(
                currency_name=currency_dict['currency'],
                currency_code=currency_dict['code'],
                currency_buy_rate=lxml_tree.xpath(
                    currency_dict['buy']
                )[0].text,
                currency_sell_rate=lxml_tree.xpath(
                    currency_dict['sell']
                )[0].text,
                bank=bank
            ))
        Currency.objects.bulk_create(found_currency_list)
    else:
        print(response.status_code)  # noqa
