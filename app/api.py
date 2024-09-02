from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi_pagination import Page, add_pagination
from sqlalchemy.orm import Session

from app import crud, models
from app.database import engine, get_db
from app.schemas import Author, AuthorCreate, Book, BookCreate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
add_pagination(app)


@app.get("/")
async def docs():
    return RedirectResponse(url='/docs')


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
