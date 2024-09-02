from sqlalchemy.orm import Session

from app import models, schemas


def create_author(db: Session, author: schemas.AuthorCreate) -> models.Author:
    author_db = models.Author(**author.model_dump())
    db_add(author_db)
    return author_db


def create_book(db: Session, book: schemas.Book) -> models.Book:
    book_db = models.Book(**book.model_dump())
    db_add(book_db)
    return book_db


def get_author(db: Session, author_id: int) -> models.Author:
    return (
        db.query(models.Author).filter(models.Author.id == author_id).first()
    )


def db_add(item: models.Author | models.Book, db: Session = Session) -> None:
    db.add(item)
    db.commit()
    db.refresh(item)
    return None
