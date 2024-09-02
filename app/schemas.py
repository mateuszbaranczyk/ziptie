from pydantic import BaseModel, Field
from typing import Optional


class BookBase(BaseModel):
    title: str = Field(max_length=128)
    genre: str = Field(max_length=32)
    pages: int
    language: str = Field(max_length=3)
    author_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str = Field(max_length=128)
    age: int
    nationality: str = Field(max_length=3)
    awards: str = Field(max_length=128)
    books: Optional[list[Book]]


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True
