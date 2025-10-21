import os
from github import Github

class GitHubManager:
    def __init__(self, repo_name: str, token: str = None):
        if token is None:
            token = os.getenv("GITHUB_TOKEN")
        if not token:
            raise ValueError("GitHub token not provided and GITHUB_TOKEN environment variable not set.")
        self.g = Github(token)
        self.repo = self.g.get_repo(repo_name)

    def create_branch(self, branch_name: str, base_branch: str = "main"):
        base_commit = self.repo.get_branch(base_branch).commit
        self.repo.create_git_ref(f"refs/heads/{branch_name}", base_commit.sha)

    def commit_file(self, branch_name: str, file_path: str, content: str, commit_message: str):
        contents = self.repo.get_contents(file_path, ref=branch_name)
        self.repo.update_file(contents.path, commit_message, content, contents.sha, branch=branch_name)

    def create_pull_request(self, title: str, body: str, head_branch: str, base_branch: str = "main"):
        pr = self.repo.create_pull(title=title, body=body, head=head_branch, base=base_branch)
        return pr.html_url

    def create_issue(self, title: str, body: str) -> str:
        issue = self.repo.create_issue(title=title, body=body)
        return issue.html_url
