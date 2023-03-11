from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Assuming the book data is stored as a list of 10 dictionaries
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"id": 6, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 7, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 8, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"id": 9, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "year": 1979},
    {"id": 10, "title": "The Shining", "author": "Stephen King", "year": 1977},
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/book/")
async def get_books():
    return books


@app.get("/book/{book_id}")
async def get_book(book_id: int):
    return books[book_id-1]