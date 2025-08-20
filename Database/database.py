from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from uuid import UUID, uuid4


DATABASE_NAME = "db.sqlite3"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

connect_args ={"check_same_thread":False} 
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args=connect_args)
SessionLocal = sessionmaker(autoflush=False,expire_on_commit=False,bind=engine)

base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


