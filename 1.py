from bs4 import BeautifulSoup
import requests


def exchange_rates(currency, format='full'):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()['Valute']
    data = response[currency]
    if format == 'full':
        return data
    elif format == 'value':
        return data['Value']


def currency_name(valute_id):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()['Valute']
    for i in response:
        if valute_id == response[i]['ID']:
            return (response[i]['Name'])


url = 'https://nplus1.ru/news/2019/06/04/slothbot'
response = requests.get(url)
page = BeautifulSoup(response.text,'html.parser')
print(page.title.text)
