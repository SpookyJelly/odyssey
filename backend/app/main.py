import requests
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.models.dto import Joke, KorJoke
from app.models.doc import doc_joke, doc_response
from app.db.db_query import count_joke_table, delete_kor_joke_table, insert_joke_table, insert_kor_joke_table, select_all_joke_table,select_all_kor_joke_table, select_kor_joke_by_id,select_kor_joke_by_ref_id,select_joke_by_id, select_random_joke_table
from app.utils.request import get_joke
from definitions import ROOT_DIR


"""
consider add api router
"""

app = FastAPI(docs_url="/odyssey/doc",redoc_url=None)


origins= ["http://localhost","http://localhost:3000","https://spookyjelly.github.io"]

app.add_middleware(
	CORSMiddleware,
	allow_origins= origins,
	allow_credentials=True,
	allow_methods =['*'],
	allow_headers=["*"]
	)
app.mount("/static",StaticFiles(directory=f"{ROOT_DIR}/app/static"),name="static")

class post_kor_joke(BaseModel):
	value:str


@app.get('/',response_class=HTMLResponse)
def main():
	return """
	    <html>
        <head>
            <title>Odyssey</title>
        </head>
        <body>
			<p>Odyssey Service is now online!</p>
        </body>
    </html>
	
	"""


@app.get('/api/search/{id}')
async def db_get(id:str):
	return select_joke_by_id(id)




	
@app.get('/api/test')
def testing_random():
	print(count_joke_table())
	return select_random_joke_table()



@app.get('/api/random',responses={200:{"model":doc_joke},404:{"model":doc_response}})
def get_simple_joke():
	try:
		# use web api unless db record less than 100
		response:Joke = get_joke().json() if count_joke_table() <= 100 else vars(select_random_joke_table())
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
		raise HTTPException(status_code=status_code, detail="external server error")


"""
번역된 내용을 DB에 넣기.
"""



#LptnivN7RPGsN3b-fSbzZA
@app.post("/api/translate/{ref_id}",responses={200:{"model":doc_response},404:{"model":doc_response}})
async def write_translated_joke(ref_id:str,post:post_kor_joke):
	eng_joke = select_joke_by_id(ref_id)
	if(not eng_joke):
		raise HTTPException(status_code=404, detail="ID doesn't exist")
	return insert_kor_joke_table(ref_id,post.value)

@app.delete("/api/translate/{id}",responses={200:{"model":doc_response},404:{"model":doc_response}})
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

 
