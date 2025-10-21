import unittest
import sqlite3
import json
from pathlib import Path
from unittest.mock import patch, MagicMock, mock_open
from datetime import datetime

from update_published_content import update_published_content_table, ARTICLE_CONTENT_PATH
from database import get_db_connection

class TestUpdatePublishedContent(unittest.TestCase):

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
                doi TEXT,
                tags TEXT
            );
        """
        )
        self.conn.commit()

        # Mock get_db_connection to return our in-memory connection
        self.mock_get_db_connection = patch('update_published_content.get_db_connection', return_value=self.conn)
        self.mock_get_db_connection.start()

        # Mock Path.glob to control which files are found
        self.mock_path_glob = patch('pathlib.Path.glob')
        self.mock_glob_instance = self.mock_path_glob.start()

    def tearDown(self):
        self.conn.close()
        self.mock_get_db_connection.stop()
        self.mock_path_glob.stop()

    @patch('builtins.open', new_callable=mock_open)
    @patch('frontmatter.load')
    def test_update_published_content_table_single_article(self, mock_frontmatter_load, mock_builtin_open):
        # Mock a Markdown file
        mock_file_path = MagicMock(spec=Path)
        mock_file_path.name = "test-article.md"
        mock_file_path.stem = "test-article"
        self.mock_glob_instance.return_value = [mock_file_path]

        # Mock frontmatter.load to return a Post object
        mock_post = MagicMock()
        mock_post.metadata = {
            'title': "Test Article Title",
            'link': "http://example.com/test-article",
            'summary': "A summary of the test article.",
            'source_name': "Test Source",
            'content_type': "blog",
            'published_date': "2025-01-01T10:00:00Z",
            'authors': ["Author One", "Author Two"],
            'doi': "10.1234/test",
            'tags': ["test", "example"]
        }
        mock_frontmatter_load.return_value = mock_post

        update_published_content_table()

        # Verify that the article was inserted into the database
        cursor = self.conn.execute("SELECT * FROM published_content")
        articles = cursor.fetchall()
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]['id'], "test-article")
        self.assertEqual(articles[0]['title'], "Test Article Title")
        self.assertEqual(articles[0]['url'], "http://example.com/test-article")
        self.assertEqual(articles[0]['summary'], "A summary of the test article.")
        self.assertEqual(articles[0]['source_name'], "Test Source")
        self.assertEqual(articles[0]['content_type'], "blog")
        self.assertEqual(articles[0]['publication_date'], "2025-01-01 10:00:00") # SQLite stores DATETIME as string
        self.assertEqual(json.loads(articles[0]['authors']), ["Author One", "Author Two"])
        self.assertEqual(articles[0]['doi'], "10.1234/test")
        self.assertEqual(json.loads(articles[0]['tags']), ["test", "example"])

    @patch('builtins.open', new_callable=mock_open)
    @patch('frontmatter.load')
    def test_update_published_content_table_duplicate_article(self, mock_frontmatter_load, mock_builtin_open):
        # Insert an article first
        self.conn.execute("""
            INSERT INTO published_content (id, title, url, summary, source_name, content_type, publication_date, authors, doi, tags)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            "test-article",
            "Existing Article",
            "http://example.com/test-article",
            "Existing Summary",
            "Existing Source",
            "blog",
            "2024-01-01 10:00:00",
            json.dumps(["Existing Author"]),
            "",
            json.dumps(["existing"])
        ))
        self.conn.commit()

        # Mock a Markdown file for the same article
        mock_file_path = MagicMock(spec=Path)
        mock_file_path.name = "test-article.md"
        mock_file_path.stem = "test-article"
        self.mock_glob_instance.return_value = [mock_file_path]

        # Mock frontmatter.load
        mock_post = MagicMock()
        mock_post.metadata = {
            'title': "Test Article Title",
            'link': "http://example.com/test-article",
            'summary': "A summary of the test article.",
            'source_name': "Test Source",
            'content_type': "blog",
            'published_date': "2025-01-01T10:00:00Z",
            'authors': ["Author One", "Author Two"],
            'doi': "10.1234/test",
            'tags': ["test", "example"]
        }
        mock_frontmatter_load.return_value = mock_post

        update_published_content_table()

        # Verify that no new article was inserted
        cursor = self.conn.execute("SELECT * FROM published_content")
        articles = cursor.fetchall()
        self.assertEqual(len(articles), 1)

    @patch('builtins.open', new_callable=mock_open)
    @patch('frontmatter.load')
    def test_update_published_content_table_missing_fields(self, mock_frontmatter_load, mock_builtin_open):
        # Mock a Markdown file with missing fields
        mock_file_path = MagicMock(spec=Path)
        mock_file_path.name = "bad-article.md"
        mock_file_path.stem = "bad-article"
        self.mock_glob_instance.return_value = [mock_file_path]

        # Mock frontmatter.load to return a Post object with missing fields
        mock_post = MagicMock()
        mock_post.metadata = {
            'title': "Bad Article",
            'link': "http://example.com/bad-article",
            # Missing summary, content_type, published_date
        }
        mock_frontmatter_load.return_value = mock_post

        update_published_content_table()

        # Verify that no article was inserted
        cursor = self.conn.execute("SELECT * FROM published_content")
        articles = cursor.fetchall()
        self.assertEqual(len(articles), 0)

    @patch('builtins.open', new_callable=mock_open)
    @patch('frontmatter.load')
    def test_update_published_content_table_authors_as_string(self, mock_frontmatter_load, mock_builtin_open):
        # Mock a Markdown file with authors as a single string
        mock_file_path = MagicMock(spec=Path)
        mock_file_path.name = "string-author-article.md"
        mock_file_path.stem = "string-author-article"
        self.mock_glob_instance.return_value = [mock_file_path]

        mock_post = MagicMock()
        mock_post.metadata = {
            'title': "String Author Article",
            'link': "http://example.com/string-author",
            'summary': "Summary.",
            'source_name': "Source",
            'content_type': "blog",
            'published_date': "2025-01-01T10:00:00Z",
            'authors': "Single Author", # Authors as a string
            'tags': ["tag1"]
        }
        mock_frontmatter_load.return_value = mock_post

        update_published_content_table()

        cursor = self.conn.execute("SELECT * FROM published_content")
        articles = cursor.fetchall()
        self.assertEqual(len(articles), 1)
        self.assertEqual(json.loads(articles[0]['authors']), ["Single Author"])

    @patch('builtins.open', new_callable=mock_open)
    @patch('frontmatter.load')
    def test_update_published_content_table_tags_as_string(self, mock_frontmatter_load, mock_builtin_open):
        # Mock a Markdown file with tags as a single string
        mock_file_path = MagicMock(spec=Path)
        mock_file_path.name = "string-tag-article.md"
        mock_file_path.stem = "string-tag-article"
        self.mock_glob_instance.return_value = [mock_file_path]

        mock_post = MagicMock()
        mock_post.metadata = {
            'title': "String Tag Article",
            'link': "http://example.com/string-tag",
            'summary': "Summary.",
            'source_name': "Source",
            'content_type': "blog",
            'published_date': "2025-01-01T10:00:00Z",
            'authors': ["Author"],
            'tags': "single-tag" # Tags as a string
        }
        mock_frontmatter_load.return_value = mock_post

        update_published_content_table()

        cursor = self.conn.execute("SELECT * FROM published_content")
        articles = cursor.fetchall()
        self.assertEqual(len(articles), 1)
        self.assertEqual(json.loads(articles[0]['tags']), ["single-tag"])
