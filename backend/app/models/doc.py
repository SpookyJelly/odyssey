from pydantic import BaseModel



class joke_eng(BaseModel):
    id:str
    url:str
    value:str
    icon_url:str
    created_at:str
    updated_at:str
    categories:list[str]

class joke_kor(BaseModel):
    id:str
    value:str
    ref_id:str
    score:int


class doc_joke(BaseModel):
    ENG: joke_eng
    KOR: list[joke_kor]

# NOTE: 에러 메지지와 단순 post response 메시지를 다르게 해야할 필요성을 못느껴서
# 기존 error reponse를 범용성 있는 이름으로 수정하여 공유 사용
class doc_response(BaseModel):
    detail: str

