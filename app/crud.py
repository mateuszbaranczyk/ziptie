from sqlalchemy.orm import Session

from app import models, schemas
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException


def create_author(author: schemas.AuthorCreate, db: Session) -> models.Author:
    author_db = models.Author(**author.model_dump())
    db_add(author_db, db)
    return author_db


def create_book(book: schemas.Book, db: Session) -> models.Book:
    book_db = models.Book(**book.model_dump())
    db_add(book_db, db)
    return book_db


def get_author(author_id: int, db: Session) -> models.Author:
    author = (
        db.query(models.Author).filter(models.Author.id == author_id).first()
    )
    if not author:
        raise HTTPException(status_code=404, detail="Not found")
    return author


def db_add(item: models.Author | models.Book, db: Session) -> None:
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Already created.")
    return None
