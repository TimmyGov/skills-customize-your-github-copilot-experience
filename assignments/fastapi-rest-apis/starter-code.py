from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str


# In-memory data store for assignment practice.
books: list[Book] = []


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/books")
def get_books() -> list[Book]:
    return books


@app.post("/books", status_code=201)
def create_book(book: Book) -> Book:
    duplicate = any(existing.id == book.id for existing in books)
    if duplicate:
        raise HTTPException(status_code=400, detail="Book with this id already exists")

    books.append(book)
    return book


# Example request:
# curl -X POST http://127.0.0.1:8000/books \
#   -H "Content-Type: application/json" \
#   -d '{"id": 1, "title": "Dune", "author": "Frank Herbert"}'
#
# Example response:
# {"id": 1, "title": "Dune", "author": "Frank Herbert"}
