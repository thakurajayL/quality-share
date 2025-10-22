import argparse
import os
from datetime import datetime
from content_extractor import extract_content
from llm_summarizer import summarize_text, generate_tags
from markdown_creator import create_markdown_content
from github_manager import GitHubManager
from database import add_visited_url, create_database
from content_classifier import classify_content, ContentType

def main():
    # Initialize the database (ensure tables exist)
    create_database()

    parser = argparse.ArgumentParser(description="Manually add an article to the curation pipeline.")
    parser.add_argument("url", type=str, help="The URL of the article to add.")
    parser.add_argument("--type", type=str, default=None, help="Override content type (e.g., BLOG_POST, RESEARCH_PAPER).")

    args = parser.parse_args()
    article_url = args.url
    content_type_override = args.type

    print(f"Processing article: {article_url}")

    # 1. Extract content
    extracted_text = extract_content(article_url)
    if not extracted_text:
        print(f"Failed to extract content from {article_url}. Exiting.")
        return

    # 2. Summarize and Tag
    summary = summarize_text(extracted_text)
    tags = generate_tags(extracted_text)

    # 3. Determine content type
    if content_type_override:
        try:
            content_type = ContentType[content_type_override.upper()]
        except KeyError:
            print(f"Invalid content type override: {content_type_override}. Using auto-detected.")
            content_type = classify_content(article_url, extracted_text)
    else:
        content_type = classify_content(article_url, extracted_text)

    # 4. Create Markdown content
    # For now, we'll use a dummy title and published date, these will be extracted later
    # from the article itself in a future story.
    title = f"Curated Article from {article_url}"
    published_date = datetime.now()

    markdown_content = create_markdown_content(title, article_url, summary, tags, published_date, content_type.name)

    # 5. GitHub Operations
    repo_name = os.getenv("GITHUB_REPO_NAME")
    if not repo_name:
        raise ValueError("GITHUB_REPO_NAME environment variable not set.")

    github_manager = GitHubManager(repo_name=repo_name)
    branch_name = f"content/new-article-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    commit_message = f"feat(content): Add new article: {title}"
    file_path = f"site/content/posts/{branch_name.replace('/', '-')}.md"

    github_manager.create_branch(branch_name)
    github_manager.commit_file(branch_name, file_path, markdown_content, commit_message)
    pr_url = github_manager.create_pull_request(f"New Curated Article: {title}", summary, branch_name)

    print(f"Pull Request created: {pr_url}")

    # 6. Add to visited URLs
    add_visited_url(article_url)
    print(f"Article {article_url} added to visited URLs.")

if __name__ == "__main__":
    main()
