import os
from datetime import datetime, timedelta
from rss_fetcher import fetch_articles
from content_extractor import extract_content
from llm_summarizer import summarize_text, generate_tags
from markdown_creator import create_markdown_content
from github_manager import GitHubManager
from database import add_visited_url, create_database
from content_classifier import classify_content

# Define the list of RSS feeds to process
RSS_FEEDS = [
    "https://engineering.fb.com/feed/",
    "http://netflixtechblog.com/feed",
    "https://eng.uber.com/feed/",
    "http://research.googleblog.com/",
    "https://openai.com/news/rss.xml",
    "https://rsshub.app/anthropic/engineering",
    "https://security.apple.com/blog/",
]

def main():
    """The main orchestration function for the AI Curation Pipeline."""
    # Initialize the database
    create_database()

    # Set a cut-off date for new articles (e.g., last 7 days)
    cut_off_date = datetime.now() - timedelta(days=7)

    print("Fetching new articles...")
    articles = fetch_articles(RSS_FEEDS, cut_off_date)
    print(f"Found {len(articles)} new articles to process.")

    if not articles:
        print("No new articles to process. Exiting.")
        return

    repo_name = os.getenv("GITHUB_REPO_NAME")
    if not repo_name:
        raise ValueError("GITHUB_REPO_NAME environment variable not set.")

    github_manager = GitHubManager(repo_name=repo_name)

    for article in articles:
        article_url = article['link']
        print(f"Processing article: {article_url}")

        try:
            # 1. Extract content
            extracted_text = extract_content(article_url)
            if not extracted_text:
                print(f"Failed to extract content from {article_url}. Skipping.")
                continue

            # 2. Summarize and Tag
            summary = summarize_text(extracted_text)
            tags = generate_tags(extracted_text)

            # 3. Determine content type
            content_type = classify_content(article_url, extracted_text)

            # 4. Create Markdown content
            title = article['title']
            published_date = article['published']
            markdown_content = create_markdown_content(title, article_url, summary, tags, published_date, content_type)

            # 5. GitHub Operations
            branch_name = f"content/new-article-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            commit_message = f"feat(content): Add new article: {title}"
            file_path = f"site/content/posts/{branch_name.replace('/', '-')}.md"

            github_manager.create_branch(branch_name)
            # We need to create the file first before we can update it.
            # A .gitkeep file is a good way to do this.
            # Let's assume for now that the file exists.
            # In a real scenario, we would need to handle file creation.
            # For this implementation, we will assume a file can be created directly.
            # The `commit_file` in the original code seems to imply an update.
            # Let's try to create the file directly.
            try:
                # Try to get the file to see if it exists. If it doesn't, create it.
                github_manager.repo.get_contents(file_path, ref=branch_name)
                github_manager.commit_file(branch_name, file_path, markdown_content, commit_message)
            except Exception:
                # If the file doesn't exist, create it.
                github_manager.repo.create_file(file_path, commit_message, markdown_content, branch=branch_name)


            pr_url = github_manager.create_pull_request(f"New Curated Article: {title}", summary, branch_name)

            print(f"Pull Request created: {pr_url}")

            # 6. Add to visited URLs
            add_visited_url(article_url)
            print(f"Article {article_url} added to visited URLs.")

        except Exception as e:
            print(f"An error occurred while processing {article_url}: {e}")
            # Optionally, create a GitHub issue to track the failure
            try:
                issue_title = f"Pipeline Error: Failed to process article {article_url}"
                issue_body = f"An error occurred during the automated pipeline execution for the article at {article_url}.\n\n**Error:**\n```\n{e}\n```"
                github_manager.create_issue(issue_title, issue_body)
                print(f"Created GitHub issue for failed article.")
            except Exception as issue_e:
                print(f"Failed to create GitHub issue for {article_url}: {issue_e}")


if __name__ == "__main__":
    main()