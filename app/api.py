from fastapi import FastAPI, Depends

from app.schemas import AuthorCreate, Author, Book, BookCreate
from app.database import engine, get_db
from app import models
from sqlalchemy.orm import Session
from app import crud
from fastapi_pagination import Page, add_pagination

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
add_pagination(app)


@app.get("/")
async def smoke():
    return {"message": "OK"}


@app.post("/author", response_model=Author)
async def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    author_db = crud.create_author(author, db)
    return author_db


@app.post("/book", response_model=Book)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    book_db = crud.create_book(book, db)
    return book_db


@app.get("/authors", response_model=Page[Author])
async def list_authors(db: Session = Depends(get_db)):
    authors = crud.list_authors(db)
    return authors
