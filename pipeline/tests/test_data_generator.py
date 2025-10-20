import unittest
import sqlite3
import json
from pathlib import Path
from unittest.mock import patch, MagicMock
from datetime import datetime

from data_generator import generate_articles_json, ARTICLES_JSON_PATH
from database import get_db_connection # Import the context manager

class TestDataGenerator(unittest.TestCase):

    def setUp(self):
        # Create a temporary in-memory database for testing
        self.conn = sqlite3.connect(":memory:")
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS published_content (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                summary TEXT,
                source_name TEXT,
                content_type TEXT NOT NULL,
                published_date DATETIME,
                authors TEXT,
                tags TEXT
            );
        """)
        self.conn.commit()

        # Mock get_db_connection to return our in-memory connection
        self.mock_get_db_connection = patch('data_generator.get_db_connection', return_value=self.conn)
        self.mock_get_db_connection.start()

        # Mock Path.mkdir to prevent actual directory creation
        self.mock_mkdir = patch('pathlib.Path.mkdir')
        self.mock_mkdir.start()

        # Mock open to capture file writes
        self.mock_open_obj = unittest.mock.mock_open()
        self.mock_open = patch('builtins.open', self.mock_open_obj)
        self.mock_open.start()
        self.mock_file_handle = self.mock_open_obj.return_value.__enter__.return_value
    def tearDown(self):
        self.conn.close()
        self.mock_get_db_connection.stop()
        self.mock_mkdir.stop()
        self.mock_open.stop()

    def test_generate_articles_json_empty(self):
        generate_articles_json()
        self.mock_file_handle.write.assert_called_once_with("[]")

    def test_generate_articles_json_with_data(self):
        # Insert some dummy data
        self.conn.execute("""
            INSERT INTO published_content (id, title, url, summary, source_name, content_type, published_date, authors, tags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "article-1",
            "Test Article 1",
            "http://example.com/article1",
            "Summary 1",
            "Source 1",
            "BLOG_POST",
            datetime(2025, 1, 1).isoformat(),
            json.dumps(["Author A"]),
            json.dumps(["tag1", "tag2"])
        ))
        self.conn.execute("""
            INSERT INTO published_content (id, title, url, summary, source_name, content_type, published_date, authors, tags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "article-2",
            "Test Article 2",
            "http://example.com/article2",
            "Summary 2",
            "Source 2",
            "RESEARCH_PAPER",
            datetime(2025, 2, 1).isoformat(),
            json.dumps(["Author B", "Author C"]),
            json.dumps(["tag3"])
        ))
        self.conn.commit()

        generate_articles_json()

        expected_data = [
            {
                "id": "article-2",
                "title": "Test Article 2",
                "url": "http://example.com/article2",
                "summary": "Summary 2",
                "source_name": "Source 2",
                "content_type": "RESEARCH_PAPER",
                "published_date": datetime(2025, 2, 1).isoformat(),
                "authors": ["Author B", "Author C"],
                "tags": ["tag3"]
            },
            {
                "id": "article-1",
                "title": "Test Article 1",
                "url": "http://example.com/article1",
                "summary": "Summary 1",
                "source_name": "Source 1",
                "content_type": "BLOG_POST",
                "published_date": datetime(2025, 1, 1).isoformat(),
                "authors": ["Author A"],
                "tags": ["tag1", "tag2"]
            }
        ]

        # Get the data that was written to the mock file
        written_data_str = "".join([call.args[0] for call in self.mock_file_handle.write.call_args_list])
        written_data = json.loads(written_data_str)

        # Assert that the written data matches the expected data
        self.assertEqual(written_data, expected_data)

if __name__ == '__main__':
    unittest.main()
