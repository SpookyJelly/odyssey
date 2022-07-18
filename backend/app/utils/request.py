import requests
import os
from app.utils.path import read_root_json

if(not os.getenv('PROD')):
    secrets = read_root_json('secrets_dev.json')
    API = secrets['API']
else:
    API = {
        'apiKey': os.getenv('RAPID_API_KEY'),
        'apihost': os.getenv('RAPID_API_HOST'),
        'apiUrl': os.getenv('RAPID_API_URL')
    }

def get_joke():
    headers = {
        "accept":"application/json",
        "X-RapidAPI-Key":API['apiKey'],
        "X-RapidAPI-Host":API['apiHost']
    }
    return requests.request("GET",API['apiUrl'],headers=headers)