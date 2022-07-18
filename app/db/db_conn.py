"""
sqlalchemy+pymysql로 DB랑 연결

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database,database_exists
from app.db.db_class import JokeTable, JokeTableKOR
from app.utils.path import read_root_json

secrets = read_root_json('secrets.json')


DB = secrets['DB']

DB_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

class engineconn:
    def __init__(self):
        # create database if not exist
        if not database_exists(DB_URL):
            create_database(DB_URL)
        self.engine = create_engine(DB_URL,pool_recycle=500)
        # create table if don't exist (using declartive model)
        # checkfirst <-- check table before execute create query
        JokeTable.__table__.create(self.engine,checkfirst=True)
        JokeTableKOR.__table__.create(self.engine,checkfirst=True)
    
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine,autocommit=False, autoflush=False)
        session =Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn
