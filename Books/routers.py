from fastapi import HTTPException,status,APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from . import models,schemas,crud
from Database import database 
import asyncio

router = APIRouter(prefix="/Books",tags=["Books"])
get_db = database.get_db

async def send_mail(book_title:str):
    await asyncio.sleep(3)
    print(f"📧 Email sent: New book added → {book_title}")

# create book
@router.post('/',response_model=schemas.BookResponse,status_code=status.HTTP_201_CREATED)
async def create_book(book:schemas.BookCreate,db:Session = Depends(get_db)):
    book = crud.create_book(db,book)
    asyncio.create_task(send_mail(book.title))
    return book

#Get all books 
@router.get("/",response_model=list[schemas.BookResponse])
async def read_book(skip:int = 0,limit:int = 0,db:Session = Depends(get_db)):
    return crud.get_books(db,skip,limit)

# Get book by ID
@router.get("/{book_id}",response_model=schemas.BookResponse)
async def read_book_by_id(book_id:int,db:Session = Depends(get_db)):
    return crud.get_book(db,book_id)

# Update book by ID
@router.put("/",response_model=schemas.BookResponse)
async def update_book(book_id:int,book:schemas.BookCreate,db:Session = Depends(get_db)):
    db_book = crud.update_book(db,book_id,book)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Book available on ID({book_id})")
    return db_book

# Delete book by ID
@router.delete("/")
async def del_book(book_id:int,db:Session = Depends(get_db)):
    db_book = crud.delete_book(db,book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Book available on ID({book_id})")
    
    return {'Message':f"{db_book.title} book deleted successfully!"}