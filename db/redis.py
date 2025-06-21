import redis

r = redis.Redis(host='redis', port=6379, decode_responses=True)

def get_availability(book_id: int):
    key = f"book:{book_id}:availability"
    value = r.get(key)
    return {"book_id": book_id, "availability": value or "unknown"}
