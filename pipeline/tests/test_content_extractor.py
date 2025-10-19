import unittest
import requests
from unittest.mock import patch, MagicMock
from content_extractor import extract_content

class TestContentExtractor(unittest.TestCase):

    @patch('requests.get')
    def test_extract_content_success(self, mock_get):
        # Mock the response from requests.get
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''
            <html>
                <head><title>My Test Page</title></head>
                <body>
                    <header>This is the header</header>
                    <main>
                        <h1>Main Title</h1>
                        <p>This is the main content of the article.</p>
                        <p>This is more content.</p>
                    </main>
                    <footer>This is the footer</footer>
                </body>
            </html>
        '''
        mock_get.return_value = mock_response

        # Call the function
        content = extract_content('http://example.com/test-page')

        # Assert the results
        self.assertIn("Main Title", content)
        self.assertIn("This is the main content of the article.", content)

    @patch('requests.get')
    def test_extract_content_request_error(self, mock_get):
        # Mock a request exception
        mock_get.side_effect = unittest.mock.Mock(side_effect=requests.exceptions.RequestException("Test Error"))

        # Call the function
        content = extract_content('http://example.com/bad-url')

        # Assert that the content is empty
        self.assertEqual(content, "")

if __name__ == '__main__':
    unittest.main()
