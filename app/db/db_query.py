from sqlalchemy import select,desc,delete
from app.db.db_conn import engineconn
from app.db.db_class import JokeTable,JokeTableKOR
from app.models.dto import Joke, KorJoke
from  sqlalchemy.sql.expression import func, select

engine = engineconn()
session = engine.sessionmaker()

def count_joke_table():
    #query object의 scalar 메서드를 사용하면 쿼리로 선택된 레코드를 스칼라 서브쿼리로 바꿔서 준다
    return session.query(func.count(JokeTable.id)).scalar()

def select_random_joke_table():
    return session.query(JokeTable).order_by(func.random()).limit(1).first()

def select_all_joke_table():
    return session.query(JokeTable).all()

def select_all_kor_joke_table():
    return session.query(JokeTableKOR).all()

def select_kor_joke_by_id(id:int):
    stmt= select("*").where(JokeTableKOR.id == id)
    return session.execute(stmt).fetchone()

def select_kor_joke_by_ref_id(id:str):
    # simple select query를 날리고 싶으면 먼저 아래와 같이 query문을 제작한 다음
    stmt= select("*").where(JokeTableKOR.ref_id == id).order_by(desc(JokeTableKOR.score))
    # session에서 execute 시키고, fetch 해야한다
    # fetchall로 하면 list 꼴로 온다
    # fetchone도 있다.이거하면 그냥 dict으로 온다
    return session.execute(stmt).fetchall()

def select_joke_by_id(id:str):
    stmt = select("*").where(JokeTable.id == id)
    return session.execute(stmt).fetchone()

def insert_joke_table(joke:Joke):
    addMemo = JokeTable(id=joke.id,updated_at=joke.updated_at,url= joke.url, value= joke.value,icon_url=joke.icon_url,categories=str(joke.categories),created_at=joke.created_at )
    session.add(addMemo)
    session.commit()
    # # TODO: commit 여부를 분기쳐서 return 메시지 수정
    return joke

def insert_kor_joke_table(ref_id:str,value:str):
    addMemo = JokeTableKOR(id=None, value=value, ref_id=ref_id,score=None)
    session.add(addMemo)
    session.commit()
    return {"detail":"success"}

def delete_kor_joke_table(id:int):
    stmt = delete(JokeTableKOR).where(JokeTableKOR.id == id)
    session.execute(stmt)
    session.commit()
    return {"detail":f"item {id} was deleted"}