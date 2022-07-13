from unicodedata import category
from wsgiref.simple_server import demo_app
import requests
from config import URL,RAPID_API_KEY,RAPID_API_HOST
from fastapi import FastAPI, HTTPException
from typing import Union
import json
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.models.models import doc_joke, doc_error_response

"""
db session
"""
from app.db.db_conn import engineconn
from app.db.db_class import JokeTable


app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

@app.get('/db')
async def db_get():
	example = session.query(JokeTable).all()
	return example


@app.post('/db/post')
async def db_post():
	addMemo = JokeTable(id=None,value='lorem')
	session.add(addMemo)
	session.commit()
	return {'message':'hoi!'}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


class Message(BaseModel):
	message: str
	message_count: float
	detail_message: str | None = None




"""
categories : Array<string>
created_at : string | date
icon_url : string
updated_at : string | date
id :string
url :string
value: string
"""

class Joke():
	# 일부 값은 None으로 유니온 해도 될까?
	id:str | None
	value:str | None
	icon_url:str | None
	url:str | None
	updated_at:str | None
	created_at:str | None
	categories:str | None
	def __init__(self, response_dict:dict):
		for arg in ['id','value','categories','icon_url','updated_at','created_at','url']:
			if arg in response_dict:
				self.__setitem__(arg,response_dict[arg])
				pass
			else:
				self.__setitem__(arg,None)

	def __setitem__ (self,k,v):
		setattr(self,k,v)



	
	

def get_joke():
	headers = {
	"accept": "application/json",
	"X-RapidAPI-Key": RAPID_API_KEY,
	"X-RapidAPI-Host": RAPID_API_HOST
	}

	#기본적으로 python의 request 모듈은 동기처리를 한
	return requests.request("GET",URL,headers=headers)





@app.get('/',responses={200:{"model":doc_joke},404:{"model":doc_error_response}})
def world():
	try:
		response = get_joke().json()
		return (Joke(response))
	except requests.exceptions.HTTPError as e:
		print('http Error?!', e)
		status_code = e.response.status_code
		raise HTTPException(status_code=status_code, detail="Item not found")


"""
번역된 내용을 DB에 넣기.
"""

"""

"""

"""

for response test

"""
@app.get('/hello')
def read_main():
	try:
		return {"msg":"Hello World"}
	except requests.exceptions.HTTPError as e:
		raise HTTPException(status_code=400,detail='error occured')

 

# response_model 지정으로 각 status마다 다른 스키마가 보일수 있도록 지정 가능 -> 여기서는 일반 response : Item 스키마, 404 일때는 Message 스키마
@app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})