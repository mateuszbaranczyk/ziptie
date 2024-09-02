from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    nationality = Column(String, nullable=False)
    awards = Column(String, nullable=False)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    language = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")
