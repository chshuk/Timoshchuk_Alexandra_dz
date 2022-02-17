import requests
from decimal import Decimal
import datetime


def currency_rates(char_code):
    """ Return name and value of currency and date"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.text
    name = None
    value = None
    today = None
    code = ">" + char_code + "<"
    for element in content.split('Valute'):
        if code.upper() in element:
            value = Decimal(element.split('Value>')[1][:-2].replace(',', '.'))
            name = element.split('Name>')[1][:-2]
        if 'Date' in element:
            today = element.split('"')[5]
    date = datetime.datetime.strptime(today, '%d.%m.%Y')

    return name, value, date or None


if __name__ == '__main__':
    dollar = currency_rates('USD')
    euro = currency_rates('EUR')
    print(f"на {dollar[2]} курс {dollar[0]} - {dollar[1]} руб")
    print(f"на {dollar[2]} курс {euro[0]} - {euro[1]} руб")
    code_valute = input('Введите код валюты:   ')
    rub = currency_rates(code_valute)
    print(rub)
