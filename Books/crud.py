from sqlalchemy.orm import Session
from . import models
from . import schemas

def create_book(db: Session, book:schemas.BookCreate):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
    
def get_books(db:Session,skip:int = 0, limit:int = 0):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db:Session,book_id:int):
    db_book = db.query(models.Book).filter(models.Book.id==book_id).first()
    if db_book:
        return db_book
    else:
        return False
    
def update_book(db:Session,book_id:int,updated_data:schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db_book.title = updated_data.title
        db_book.author = updated_data.author
        db_book.description = updated_data.description
        
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db:Session,book_id:int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book