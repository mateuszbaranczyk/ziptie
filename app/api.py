from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def smoke():
    return {"message": "OK"}


@app.post("/author")
async def create_author():
    pass


@app.post("/book")
async def create_book():
    pass


@app.get("/author-books/{author_id}")
async def get_author_books(author_id: int):
    pass
