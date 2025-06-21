from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://mongodb:27017")
db = client.library_db

async def get_reviews(book_id: int):
    reviews_cursor = db.reviews.find({"book_id": book_id})
    reviews = []
    async for review in reviews_cursor:
        review["_id"] = str(review["_id"])
        reviews.append(review)
    return reviews
