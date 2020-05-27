from bs4 import BeautifulSoup
from pprint import pprint
import requests
import pandas as pd


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


def wiki_header(url):
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    return (page.find('h1').text)


def vk_male_female():
    url = 'https://api.vk.com/method/users.get'
    ids = ','.join(map(str, range(1, 501)))
    params = {'user_ids': ids, 'v': 5.103, 'fields': 'sex',
              'access_token': 'fb78135efb78135efb78135e88fb0a0e02ffb78fb78135ea5bfbc00899d31ae0f264df2'}
    response = requests.get(url, params=params)
    users = response.json()['response']
    f = 0
    m = 0
    for i in users:
        if i['sex'] == 1:
            f += 1
        elif i['sex'] == 2:
            m += 1
    print(f / (m + f))


def get_actors(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    page_1 = BeautifulSoup(response.text, 'html.parser')
    # page_2 = page_1.find_all('div', id='actorList')
    # actors = page_2.find_all('a').text
    # return actors
    pprint(page_1)


def vk_get_smm_index(group_name, token):
    url_smm = 'https://api.vk.com/method/wall.get'
    url_count = 'https://api.vk.com/method/groups.getMembers'
    param = {'domain': group_name,
             'filter': 'owner',
             'count': 10,
             'offset': 0,
             'extended': 1,
             'v': 5.107,
             'access_token': token}
    response = requests.get(url_smm, params=param)
    likes = 0
    comments = 0
    reposts = 0
    group_id = response.json()['response']['groups'][0]['id']
    param_count = {'group_id': group_id,
                   'v': 5.107,
                   'access_token': token}
    count = requests.get(url_count, params=param_count)
    members = int(count.json()['response']['count'])
    for record in response.json()['response']['items'][:]:
        title = record['text'][:30]
        if title:
            comments += int(record['comments']['count'])
            likes += int(record['likes']['count'])
            reposts += int(record['reposts']['count'])
    smm_index = (comments + likes + reposts) / members
    return smm_index
