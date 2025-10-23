import unittest
import sqlite3
import json
from pathlib import Path
from unittest.mock import patch, MagicMock, call
from datetime import datetime

from data_generator import generate_articles_json_and_markdown, ARTICLES_JSON_PATH, ARTICLE_CONTENT_PATH
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
                publication_date DATETIME,
                authors TEXT,
                tags TEXT
            );
        """
        )
        self.conn.commit()

        # Mock get_db_connection to return our in-memory connection
        self.mock_get_db_connection = patch('data_generator.get_db_connection', return_value=self.conn)
        self.mock_get_db_connection.start()

        # Mock Path.mkdir to prevent actual directory creation
        self.mock_mkdir = patch('pathlib.Path.mkdir')
        self.mock_mkdir.start()

        # Mock json.dump to capture the data written to articles.json
        self.patch_json_dump = patch('data_generator.json.dump')
        self.mock_json_dump = self.patch_json_dump.start()

    def tearDown(self):
        self.conn.close()
        self.mock_get_db_connection.stop()
        self.mock_mkdir.stop()
        self.patch_json_dump.stop()

    def test_generate_articles_json_empty(self):
        generate_articles_json_and_markdown()
        self.mock_json_dump.assert_called_once_with([], unittest.mock.ANY, indent=4)

    def test_generate_articles_json_with_data(self):
        # Insert some dummy data
                self.conn.execute("""
                    INSERT INTO published_content (id, title, url, summary, source_name, content_type, publication_date, authors, tags)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    "article-1",
                    "Test Article 1",
                    "http://example.com/article1",
                    "Summary 1",
                    "Source 1",
                    "BLOG_POST",
                    datetime(2025, 1, 1),
                    json.dumps(["Author A"]),
                    json.dumps(["tag1", "tag2"])
                ))
                self.conn.execute("""
                    INSERT INTO published_content (id, title, url, summary, source_name, content_type, publication_date, authors, tags)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    "article-2",
                    "Test Article 2",
                    "http://example.com/article2",
                    "Summary 2",
                    "Source 2",
                    "RESEARCH_PAPER",
                    datetime(2025, 2, 1),
                    json.dumps(["Author B", "Author C"]),
                    json.dumps(["tag3"])
                ))
                self.conn.commit()
        
                generate_articles_json_and_markdown()
        
                expected_json_data = [
                    {
                        "title": "Test Article 2",
                        "link": "http://example.com/article2",
                        "summary": "Summary 2",
                        "tags": ["tag3"],
                        "date": datetime(2025, 2, 1).isoformat(),
                        "content_type": "RESEARCH_PAPER",
                        "authors": ["Author B", "Author C"],
                        "doi": None
                    },
                    {
                        "title": "Test Article 1",
                        "link": "http://example.com/article1",
                        "summary": "Summary 1",
                        "tags": ["tag1", "tag2"],
                        "date": datetime(2025, 1, 1).isoformat(),
                        "content_type": "BLOG_POST",
                        "authors": ["Author A"],
                        "doi": None
                    }
                ]
        
                # Assert that the JSON file was written correctly
                self.mock_json_dump.assert_called_once_with(expected_json_data, unittest.mock.ANY, indent=4)
if __name__ == '__main__':
    unittest.main()
