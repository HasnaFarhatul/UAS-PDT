from fastapi import FastAPI
from db.postgres import get_books
from db.mongodb import get_reviews
from db.redis import get_availability

app = FastAPI()

@app.get("/books/search")
async def search_books(title: str):
    return await get_books(title)

@app.get("/books/{book_id}/reviews")
async def reviews(book_id: int):
    return await get_reviews(book_id)

@app.get("/books/{book_id}/availability")
async def availability(book_id: int):
    return get_availability(book_id)
