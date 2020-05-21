import requests
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url).json()['Valute']
valute_id = 'R01700J'
for i in response:
    if valute_id==response[i]['ID']:
        print(response[i]['Name'])
#print (response)