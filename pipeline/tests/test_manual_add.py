import unittest
from unittest.mock import patch, MagicMock
import os
from datetime import datetime

# Mock the main function to prevent it from running during import
@patch('manual_add.main')
def test_main_mock(mock_main):
    pass

class TestManualAddScript(unittest.TestCase):

    @patch('manual_add.create_database')
    @patch('manual_add.add_visited_url')
    @patch('manual_add.GitHubManager')
    @patch('manual_add.create_markdown_content')
    @patch('manual_add.generate_tags')
    @patch('manual_add.summarize_text')
    @patch('manual_add.extract_content')
    @patch.dict(os.environ, {'GITHUB_TOKEN': 'test_token', 'GITHUB_REPO_NAME': 'test-repo'})
    def test_main_script_flow(self, mock_extract_content, mock_summarize_text, mock_generate_tags,
                              mock_create_markdown_content, MockGitHubManager, mock_add_visited_url, mock_create_database):

        # Mock return values
        mock_extract_content.return_value = "Extracted content"
        mock_summarize_text.return_value = "Concise summary"
        mock_generate_tags.return_value = ["tag1", "tag2"]
        mock_create_markdown_content.return_value = "---\ntitle: Test\n---"
        mock_github_manager_instance = MagicMock()
        MockGitHubManager.return_value = mock_github_manager_instance
        mock_github_manager_instance.create_pull_request.return_value = "http://pr-url.com"

        # Simulate command-line arguments
        with patch('argparse.ArgumentParser.parse_args', return_value=MagicMock(url="http://example.com/article", type=None)):
            # Run the script
            import manual_add
            manual_add.main()

            # Assertions
            mock_create_database.assert_called_once()
            mock_extract_content.assert_called_once_with("http://example.com/article")
            mock_summarize_text.assert_called_once_with("Extracted content")
            mock_generate_tags.assert_called_once_with("Extracted content")
            mock_create_markdown_content.assert_called_once()
            MockGitHubManager.assert_called_once_with(repo_name="test-repo")
            mock_github_manager_instance.create_branch.assert_called_once()
            mock_github_manager_instance.commit_file.assert_called_once()
            mock_github_manager_instance.create_pull_request.assert_called_once()
            mock_add_visited_url.assert_called_once_with("http://example.com/article")

    @patch('manual_add.create_database')
    @patch('manual_add.add_visited_url')
    @patch('manual_add.GitHubManager')
    @patch('manual_add.create_markdown_content')
    @patch('manual_add.generate_tags')
    @patch('manual_add.summarize_text')
    @patch('manual_add.extract_content', return_value="") # Simulate failed extraction
    @patch.dict(os.environ, {'GITHUB_TOKEN': 'test_token', 'GITHUB_REPO_NAME': 'test-repo'})
    def test_main_script_flow_no_content(self, mock_extract_content, mock_summarize_text, mock_generate_tags,
                                        mock_create_markdown_content, MockGitHubManager, mock_add_visited_url, mock_create_database):

        with patch('argparse.ArgumentParser.parse_args', return_value=MagicMock(url="http://example.com/article", type=None)):
            import manual_add
            manual_add.main()

            mock_extract_content.assert_called_once_with("http://example.com/article")
            mock_summarize_text.assert_not_called()
            mock_generate_tags.assert_not_called()
            mock_create_markdown_content.assert_not_called()
            MockGitHubManager.assert_not_called()
            mock_add_visited_url.assert_not_called()

if __name__ == '__main__':
    unittest.main()
