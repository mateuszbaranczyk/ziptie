from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)

    name = Column(String(length=128), nullable=False)
    age = Column(Integer, nullable=False)
    nationality = Column(String(length=3), nullable=False)
    awards = Column(String(length=256), nullable=False)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)

    title = Column(String(length=128), nullable=False)
    genre = Column(String(length=32), nullable=False)
    pages = Column(Integer, nullable=False)
    language = Column(String(length=3), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")
