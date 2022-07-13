"""
상속된 클래스들을 자동으로 매핑

"""
from sqlalchemy import Column,TEXT,INT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class JokeTable(Base):
    __tablename__ = 'joke'
    id = Column(INT,nullable=False, autoincrement=True, primary_key=True)
    value = Column(TEXT,nullable=False)