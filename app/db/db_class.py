"""
상속된 클래스들을 자동으로 매핑

"""
from sqlalchemy import Column,TEXT,INT,ForeignKey,VARCHAR,TIMESTAMP,SMALLINT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class JokeTable(Base):
    __tablename__ = 'joke'
    # db 테이블에 저장되는 아이디인데 나눌 필요가 있나? 생각해보니?
    # id가 무조건 숫자로 되야한다는 것을 버려라
    # id = Column(INT,nullable=False, autoincrement=True, primary_key=True)
    # value = Column(TEXT,nullable=False)
    # # uuid => Joke response로 오는 응답에서의 id
    # uuid = Column(VARCHAR(128),nullable=False)
    id = Column(VARCHAR(128), primary_key=True )
    categories = Column(VARCHAR(128))
    created_at = Column(TIMESTAMP())
    updated_at = Column (TIMESTAMP())
    value = Column(TEXT(), nullable= False)
    url = Column(VARCHAR(2083))
    icon_url = Column(VARCHAR(2083))

class JokeTableKOR(Base):
    __tablename__='kor_joke'
    id = Column(INT, nullable=False, autoincrement = True, primary_key= True)
    ref_id = Column(VARCHAR(128),ForeignKey('joke.id'))
    value = Column(VARCHAR(256), nullable= False)
    score = Column(SMALLINT, default=0)