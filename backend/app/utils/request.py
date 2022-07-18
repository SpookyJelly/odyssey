import requests
from app.utils.path import read_root_json

secrets = read_root_json('secrets.json')
API = secrets['API']

def get_joke():
    headers = {
        "accept":"application/json",
        "X-RapidAPI-Key":API['apiKey'],
        "X-RapidAPI-Host":API['apiHost']
    }
    return requests.request("GET",API['apiUrl'],headers=headers)