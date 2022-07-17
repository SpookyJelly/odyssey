import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.models.dto import Joke, KorJoke
from app.models.doc import doc_joke, doc_response
from app.db.db_query import delete_kor_joke_table, insert_joke_table, insert_kor_joke_table, select_all_joke_table,select_all_kor_joke_table, select_kor_joke_by_id,select_kor_joke_by_ref_id,select_joke_by_id
from app.utils.request import get_joke


"""
consider add api router
"""

app = FastAPI()


origins= ["http://localhost","http://localhost:3000"]

app.add_middleware(
	CORSMiddleware,
	allow_origins= origins,
	allow_credentials=True,
	allow_methods =['*'],
	allow_headers=["*"]
	)

class post_kor_joke(BaseModel):
	value:str



@app.get('/db')
async def db_get():
	return select_joke_by_id('abc')


# # example 
# # @app.post('/db/post',responses={200:{'model':doc_joke}})
# @app.post('/db/post')
# async def db_post(post:Post):
# 	addMemo = joke_table(id=None, value= post.value)
# 	session.add(addMemo)
# 	session.commit()
# 	return post

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []




	
	

# def get_joke():
# 	headers = {
# 	"accept": "application/json",
# 	"X-RapidAPI-Key": RAPID_API_KEY,
# 	"X-RapidAPI-Host": RAPID_API_HOST
# 	}

# 	#기본적으로 python의 request 모듈은 동기처리를 한
# 	return requests.request("GET",URL,headers=headers)





@app.get('/',responses={200:{"model":doc_joke},404:{"model":doc_response}})
def get_simple_joke():
	try:
		response:Joke = get_joke().json()
		kor_res:list[KorJoke] = select_kor_joke_by_ref_id(response['id'])
		if(not kor_res):
			en_res:Joke = select_joke_by_id(response['id'])
			if (not en_res):
				insert_joke_table(Joke(response))
			return {
				"ENG":response,
				"KOR":[]
			}
		# return value when translate value exist
		return {
			"ENG":response,
			"KOR": kor_res
			}

	except requests.exceptions.HTTPError as e:
		print('http Error?!', e)
		status_code = e.response.status_code
		raise HTTPException(status_code=status_code, detail="Item not found")


"""
번역된 내용을 DB에 넣기.
"""



#LptnivN7RPGsN3b-fSbzZA
@app.post("/translate/{ref_id}",responses={200:{"model":doc_response},404:{"model":doc_response}})
async def write_translated_joke(ref_id:str,post:post_kor_joke):
	eng_joke = select_joke_by_id(ref_id)
	if(not eng_joke):
		raise HTTPException(status_code=404, detail="ID doesn't exist")
	return insert_kor_joke_table(ref_id,post.value)

@app.delete("/translate/{id}",responses={200:{"model":doc_response},404:{"model":doc_response}})
async def delete_translated_joke(id:int):
	kor_joke = select_kor_joke_by_id(id)
	if(not kor_joke):
		raise HTTPException(status_code=404 , detail=f"ID {id} kor joke doesn't exist")
	#try catch?
	return delete_kor_joke_table(id)

"""

for response test

"""
@app.get('/hello')
def read_main():
	try:
		return {"msg":"Hello World"}
	except requests.exceptions.HTTPError as e:
		raise HTTPException(status_code=400,detail='error occured')

 

# # response_model 지정으로 각 status마다 다른 스키마가 보일수 있도록 지정 가능 -> 여기서는 일반 response : Item 스키마, 404 일때는 Message 스키마
# @app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
# async def read_item(item_id: str):
#     if item_id == "foo":
#         return {"id": "foo", "value": "there goes my hero"}
#     else:
#         return JSONResponse(status_code=404, content={"message": "Item not found"})