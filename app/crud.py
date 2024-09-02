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


def get_author(author_id: int, db: Session) -> models.Author:
    return (
        db.query(models.Author).filter(models.Author.id == author_id).first()
    )


def db_add(item: models.Author | models.Book, db: Session) -> None:
    db.add(item)
    db.commit()
    db.refresh(item)
    return None
