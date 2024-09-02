from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    genre: str
    pages: int
    language: str


class Author(BaseModel):
    id: int
    name: str
    age: int
    nationality: str
    awards: str

    books: list[Book]
