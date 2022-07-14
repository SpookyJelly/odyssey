"""
상속된 클래스들을 자동으로 매핑

"""
from sqlalchemy import Column,TEXT,INT,ForeignKey,VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class joke_table(Base):
    __tablename__ = 'joke'
    # db 테이블에 저장되는 아이디인데 나눌 필요가 있나? 생각해보니?
    # id가 무조건 숫자로 되야한다는 것을 버려라
    id = Column(INT,nullable=False, autoincrement=True, primary_key=True)
    value = Column(TEXT,nullable=False)
    # uuid => Joke response로 오는 응답에서의 id
    uuid = Column(VARCHAR(128),nullable=False)

class kor_joke_table(Base):
    __tablename__='kor_joke'
    id = Column(INT, nullable=False, autoincrement = True, primary_key= True)
    ref_id = Column(VARCHAR(128),ForeignKey('joke.uuid'))