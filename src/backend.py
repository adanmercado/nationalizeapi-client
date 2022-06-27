import requests, json

API_URL = 'https://api.nationalize.io/'

def search_name(name: str) -> list:
    countries = []
    if not name:
        return countries

    try:
        response = requests.get(API_URL, params={'name': name})
        if response.status_code == 200:
            data = json.loads(response.text)
            if data:
                countries = data['country']
        return countries
    except:
        print('An error ocurred.')
        return countries