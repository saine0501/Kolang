from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv("DB_USER")     # "root"
passwd = os.getenv("DB_PASSWD") # "1234"
host = os.getenv("DB_HOST")     # "localhost"
port = os.getenv("DB_PORT")     # "3306"
db = os.getenv("DB_NAME")       # "kolang"

DB_URL = f'mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8'

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()