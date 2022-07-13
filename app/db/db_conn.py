"""
sqlalchemy+pymysql로 DB랑 연결

"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.utils.path import read_root_json
secrets = read_root_json('secrets.json')


DB = secrets['DB']

DB_URL = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL,pool_recycle=500)
    
    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine,autocommit=False, autoflush=False)
        session =Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn
