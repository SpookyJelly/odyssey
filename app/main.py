from unicodedata import category
from wsgiref.simple_server import demo_app
import requests
from config import URL,RAPID_API_KEY,RAPID_API_HOST
from fastapi import FastAPI, HTTPException
from typing import Union
import json
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.db.models import doc_joke, doc_error_response

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



app = FastAPI()

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
	id:str
	value:str
	icon_url:str
	url:str
	updated_at:str
	created_at:str
	categories:str
	def __init__(self, response_dict:dict):
		for arg in ['id','value','categories','icon_url','updated_at','created_at','url']:
			if arg in response_dict:
				self.__setitem__(arg,response_dict[arg])
				pass
			else:
				self.__setitem__(arg,'lorem')

	def __setitem__ (self,k,v):
		setattr(self,k,v)



	
	

# 요청 보내는 부분과 그걸 인스턴스로 바꾸는건 또 다른 함수로 빼야한다.
# 그래야 테스트가 쉬움
# 그것도 따로 테스트로
def get_joke():
	headers = {
	"accept": "application/json",
	"X-RapidAPI-Key": RAPID_API_KEY,
	"X-RapidAPI-Host": RAPID_API_HOST
	}

	#기본적으로 python의 request 모듈은 동기처리를 한
	return requests.request("GET",URL,headers=headers)

	# get_joke 에서 try except 처리가 필요
	# 그러면 코드레벨에서 강제로 에러를 만들어야하나늗네...
	#try
	# except : httpException 하고 testcode 자체에서도 분기처리?





@app.get('/',responses={200:{"model":doc_joke},404:{"model":doc_error_response}})
def world():
	try:
		response = get_joke().json()
		return (Joke(response))
	except requests.exceptions.HTTPError as e:
		print('http Error?!', e)
		status_code = e.response.status_code
		raise HTTPException(status_code=status_code, detail="Item not found")

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