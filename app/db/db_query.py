from sqlalchemy import select
from app.db.db_conn import engineconn
from app.db.db_class import JokeTable,JokeTableKOR
from app.models.dto import Joke

engine = engineconn()
session = engine.sessionmaker()

def select_all_joke_table():
    return session.query(JokeTable).all()

def select_all_kor_joke_table():
    return session.query(JokeTableKOR).all()

def select_kor_joke_by_id(id:str):
    # simple select query를 날리고 싶으면 먼저 아래와 같이 query문을 제작한 다음
    stmt= select("*").where(JokeTableKOR.ref_id == id)
    # session에서 execute 시키고, fetch 해야한다
    # fetchall로 하면 list 꼴로 온다
    # fetchone도 있다.이거하면 그냥 dict으로 온다
    return session.execute(stmt).fetchall()

def select_joke_by_id(id:str):
    stmt = select("*").where(JokeTable.id == id)
    return session.execute(stmt).fetchone()

def insert_joke_table(joke:Joke):
    # print(joke)
    addMemo = JokeTable(id=joke.id,updated_at=joke.updated_at,url= joke.url, value= joke.value,icon_url=joke.icon_url,categories=str(joke.categories),created_at=joke.created_at )
    session.add(addMemo)
    session.commit()
    # # TODO: commit 여부를 분기쳐서 return 메시지 수정
    return joke