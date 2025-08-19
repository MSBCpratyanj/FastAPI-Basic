from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autoflush=False,expire_on_commit=False,bind=engine)

base = declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    except:
        print("DB connection fail")
    finally:
        db.close()