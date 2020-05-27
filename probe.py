import requests
from pprint import pprint

def get_smm_index(group_name,token):
    url_smm = 'https://api.vk.com/method/wall.get'
    url_count = 'https://api.vk.com/method/groups.getMembers'
    param = {'domain': group_name,
             'filter': 'owner',
             'count': 10,
             'offset': 0,
             'extended':1,
             'v': 5.107,
             'access_token': token}
    response = requests.get(url_smm, params=param)
    likes = 0
    comments = 0
    reposts = 0
    group_id=response.json()['response']['groups'][0]['id']
    param_count = {'group_id':group_id,
                   'v':5.107,
                   'access_token': token}
    count = requests.get(url_count,params=param_count)
    members = int(count.json()['response']['count'])
    for record in response.json()['response']['items'][:]:
        title = record['text'][:30]
        if title:
            comments+= int(record['comments']['count'])
            likes+=int(record['likes']['count'])
            reposts+=int(record['reposts']['count'])
    smm_index= (comments+likes+reposts)/members
    return smm_index
get_smm_index('habr','fb78135efb78135efb78135e88fb0a0e02ffb78fb78135ea5bfbc00899d31ae0f264df2')