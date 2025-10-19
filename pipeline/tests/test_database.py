import unittest
import sqlite3
from database import _add_visited_url, _is_url_visited

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Set up an in-memory SQLite database for testing."""
        self.conn = sqlite3.connect(":memory:")
        # Create the table
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS visited_urls (
                url TEXT PRIMARY KEY,
                visited_at DATETIME NOT NULL
            );
        """)
        self.conn.commit()

    def tearDown(self):
        """Close the database connection after each test."""
        self.conn.close()

    def test_add_and_is_visited(self):
        """Test adding a URL and checking if it has been visited."""
        # First, check that the URL is not visited
        self.assertFalse(_is_url_visited(self.conn, 'http://example.com/1'))

        # Add the URL
        _add_visited_url(self.conn, 'http://example.com/1')

        # Now, check that the URL is visited
        self.assertTrue(_is_url_visited(self.conn, 'http://example.com/1'))

    def test_is_url_visited_for_non_existent_url(self):
        """Test checking a URL that has not been visited."""
        self.assertFalse(_is_url_visited(self.conn, 'http://example.com/non-existent'))

if __name__ == '__main__':
    unittest.main()