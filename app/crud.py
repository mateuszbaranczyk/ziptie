from fastapi import HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import models, schemas


def create_author(author: schemas.AuthorCreate, db: Session) -> models.Author:
    author_db = models.Author(**author.model_dump())
    db_add(author_db, db)
    return author_db


def create_book(book: schemas.Book, db: Session) -> models.Book:
    book_db = models.Book(**book.model_dump())
    db_add(book_db, db)
    return book_db


def list_authors(db: Session) -> Page[models.Author]:
    authors = paginate(db, select(models.Author).order_by(models.Author.name))
    return authors


def db_add(item: models.Author | models.Book, db: Session) -> None:
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Already created.")
    return None
