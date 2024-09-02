from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    genre: str
    pages: int
    language: str
    author_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str
    age: int
    nationality: str
    awards: str
    books: Optional[list[Book]] = []


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True
