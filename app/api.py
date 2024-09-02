from fastapi import FastAPI, Depends

from app.schemas import AuthorCreate, Author, Book, BookCreate
from app.database import engine, get_db
from app import models
from sqlalchemy.orm import Session
from app.crud import create_author, create_book, get_author

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def smoke():
    return {"message": "OK"}


@app.post("/author", response_model=Author)
async def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    author_db = create_author(author, db)
    return author_db


@app.post("/book", response_model=Book)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    book_db = create_book(book)
    return book_db


@app.get("/author-books/{author_id}", response_model=Author)
async def get_author_books(author_id: int):
    author_db = get_author(author_id)
    return author_db
