import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        dbname="library_db",
        user="user",
        password="password",
        host="postgres",
        port="5432"
    )

async def get_books(title: str):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM books WHERE title ILIKE %s;", (f"%{title}%",))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
