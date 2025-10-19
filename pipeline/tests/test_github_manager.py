import unittest
import os
from unittest.mock import patch, MagicMock
from github_manager import GitHubManager

class TestGitHubManager(unittest.TestCase):

    @patch('github_manager.Github')
    @patch.dict(os.environ, {'GITHUB_TOKEN': 'test_token'})
    def setUp(self, MockGithub):
        self.mock_github_instance = MockGithub.return_value
        self.mock_repo = MagicMock()
        self.mock_github_instance.get_user.return_value.get_repo.return_value = self.mock_repo
        self.manager = GitHubManager(repo_name="test-repo")

    def test_create_branch(self):
        self.mock_repo.get_git_ref.return_value.sha = "12345"
        self.manager.create_branch("new-branch")
        self.mock_repo.create_git_ref.assert_called_once_with("refs/heads/new-branch", "12345")

    def test_commit_file(self):
        mock_contents = MagicMock()
        mock_contents.path = "test.md"
        mock_contents.sha = "old_sha"
        self.mock_repo.get_contents.return_value = mock_contents
        self.manager.commit_file("new-branch", "test.md", "new content", "commit message")
        self.mock_repo.update_file.assert_called_once_with("test.md", "commit message", "new content", "old_sha", branch="new-branch")

    def test_create_pull_request(self):
        mock_pr = MagicMock()
        mock_pr.html_url = "http://github.com/pr/1"
        self.mock_repo.create_pull.return_value = mock_pr
        pr_url = self.manager.create_pull_request("PR Title", "PR Body", "head-branch")
        self.assertEqual(pr_url, "http://github.com/pr/1")
        self.mock_repo.create_pull.assert_called_once_with(title="PR Title", body="PR Body", head="head-branch", base="main")

    @patch.dict(os.environ, {}, clear=True)
    def test_init_no_token(self):
        with self.assertRaises(ValueError) as cm:
            GitHubManager(repo_name="test-repo")
        self.assertEqual(str(cm.exception), "GitHub token not provided and GITHUB_TOKEN environment variable not set.")

if __name__ == '__main__':
    unittest.main()
