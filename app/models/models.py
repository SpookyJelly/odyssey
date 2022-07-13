from pydantic import BaseModel

class doc_joke(BaseModel):
    id: str
    url: str
    value: str
    icon_url:str
    created_at:str
    updated_at:str
    categories: list[str] | None

class doc_error_response(BaseModel):
    detail: str
    code: int


