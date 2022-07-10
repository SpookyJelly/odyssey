import requests
from config import URL,RAPID_API_KEY,RAPID_API_HOST
from fastapi import FastAPI
from typing import Union
import json
from pprint import pprint

app = FastAPI()

class Joke:
	def __init__(self, id,value):
		self.id = id
		self.value = value

	


def get_joke():
	headers = {
	"accept": "application/json",
	"X-RapidAPI-Key": RAPID_API_KEY,
	"X-RapidAPI-Host": RAPID_API_HOST
	}

	response = requests.request("GET", URL, headers=headers)
	test = json.loads(response.text)
	pprint(response.text)
	print('hoi',test['value'])

	joke_instance = Joke(test['id'],test['value'])
	print('joke_instance',joke_instance.id)
	print('joke_instance_2',joke_instance.value)





@app.get('/')
def world():
	get_joke()
	return {'value':'hello world'}





