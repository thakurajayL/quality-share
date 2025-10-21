import sqlite3
from pathlib import Path
from contextlib import contextmanager

DATABASE_PATH = Path(__file__).parent.parent / "data" / "pipeline.db"

@contextmanager
def get_db_connection():
    """Gets a connection to the SQLite database, handling setup and teardown."""
    DATABASE_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def create_database():
    """Creates the database and the visited_urls table if they don't exist."""
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS visited_urls (
                url TEXT PRIMARY KEY,
                visited_at DATETIME NOT NULL
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS published_content (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                summary TEXT,
                source_name TEXT,
                content_type TEXT NOT NULL,
                publication_date DATETIME,
                authors TEXT, -- Stored as a JSON array
                doi TEXT,
                tags TEXT -- Stored as a JSON array
            );
        """)
        conn.commit()

def _add_visited_url(conn, url: str):
    """Core logic to add a new URL to the visited_urls table."""
    conn.execute("INSERT INTO visited_urls (url, visited_at) VALUES (?, datetime('now'))", (url,))
    conn.commit()

def add_visited_url(url: str):
    """Adds a new URL to the visited_urls table."""
    with get_db_connection() as conn:
        _add_visited_url(conn, url)

def _is_url_visited(conn, url: str) -> bool:
    """Core logic to check if a URL already exists in the visited_urls table."""
    cursor = conn.execute("SELECT 1 FROM visited_urls WHERE url = ?", (url,))
    result = cursor.fetchone()
    return result is not None

def is_url_visited(url: str) -> bool:
    """Checks if a URL already exists in the visited_urls table."""
    with get_db_connection() as conn:
        return _is_url_visited(conn, url)