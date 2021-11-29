import requests


YANDEX_TOKEN = ''
url = "https://cloud-api.yandex.net/v1/disk/resources"

def create_path(name):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': YANDEX_TOKEN
        }
        params = {'path' : name}
        response = requests.put(url = url, headers = headers, params = params)
        if response.status_code == 201:
            print('Created')
        return response.status_code
