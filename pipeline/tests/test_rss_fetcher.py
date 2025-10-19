import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from rss_fetcher import fetch_articles

class TestRssFetcher(unittest.TestCase):

    @patch('rss_fetcher.is_url_visited', return_value=False)
    @patch('feedparser.parse')
    def test_fetch_articles_with_no_visited_urls(self, mock_parse, mock_is_visited):
        # Mock the RSS feed data
        mock_feed = MagicMock()
        mock_feed.entries = [
            {
                'title': 'Article 1',
                'link': 'http://example.com/1',
                'published': '2025-10-15T12:00:00Z',
            },
            {
                'title': 'Article 2',
                'link': 'http://example.com/2',
                'published': '2025-09-30T12:00:00Z', # This one is before the cut-off
            },
            {
                'title': 'Article 3',
                'link': 'http://example.com/3',
                'published': '2025-10-20T12:00:00Z',
            },
        ]
        mock_parse.return_value = mock_feed

        # Set the cut-off date
        cut_off_date = datetime(2025, 10, 1)

        # Call the function
        articles = fetch_articles(['http://example.com/feed'], cut_off_date)

        # Assert the results
        self.assertEqual(len(articles), 2)
        self.assertEqual(articles[0]['title'], 'Article 1')
        self.assertEqual(articles[1]['title'], 'Article 3')

    @patch('rss_fetcher.is_url_visited', side_effect=lambda url: url == 'http://example.com/1')
    @patch('feedparser.parse')
    def test_fetch_articles_with_one_visited_url(self, mock_parse, mock_is_visited):
        # Mock the RSS feed data
        mock_feed = MagicMock()
        mock_feed.entries = [
            {
                'title': 'Article 1',
                'link': 'http://example.com/1',
                'published': '2025-10-15T12:00:00Z',
            },
            {
                'title': 'Article 2',
                'link': 'http://example.com/2',
                'published': '2025-09-30T12:00:00Z', # This one is before the cut-off
            },
            {
                'title': 'Article 3',
                'link': 'http://example.com/3',
                'published': '2025-10-20T12:00:00Z',
            },
        ]
        mock_parse.return_value = mock_feed

        # Set the cut-off date
        cut_off_date = datetime(2025, 10, 1)

        # Call the function
        articles = fetch_articles(['http://example.com/feed'], cut_off_date)

        # Assert the results
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0]['title'], 'Article 3')

if __name__ == '__main__':
    unittest.main()
