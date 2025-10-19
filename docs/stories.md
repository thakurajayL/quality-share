# Product Backlog

This document contains the user stories for the Quality Share project, organized by epic.

---

## Epic 1: Project Foundation & Setup

*   **Story 1.1:** As the project owner, I want the `source-tree` directory structure created in the repository, so that we have a clean and organized codebase.
*   **Story 1.2:** As a developer, I want a new Python project initialized with Poetry in the `pipeline` directory, so that I can start developing the AI Curation Pipeline.
*   **Story 1.3:** As the project owner, I want a basic Hugo site initialized in the `site` directory, so that we have a starting point for the website.
*   **Story 1.4:** As a developer, I want a basic CI/CD pipeline that automatically builds and deploys the Hugo site to GitHub Pages on every push to the `main` branch.
*   **Story 1.5:** As a developer, I want a basic testing workflow that runs `pytest` on every Pull Request to ensure code quality.

---

## Epic 2: AI Curation Pipeline (MVP)

*   **Story 2.1:** As a developer, I want the pipeline to fetch the latest articles from a list of RSS feeds, so that we have a source of content to process.
*   **Story 2.2:** As a developer, I want the pipeline to check a SQLite database of visited URLs before processing an article, so that we don't create duplicate content.
*   **Story 2.3a:** As a developer, I want a function that can take a URL and extract the clean, main body of text from the article, stripping away boilerplate like headers, footers, and ads.
*   **Story 2.3b:** As a developer, I want a function that can take the extracted text and send it to an LLM to generate a concise summary.
*   **Story 2.3c:** As a developer, I want a function that can take the extracted text and send it to an LLM to generate a list of relevant tags.
*   **Story 2.4:** As a developer, I want the pipeline to create a new Markdown file with the processed content (title, summary, tags, etc.) formatted as front matter.
*   **Story 2.5:** As a developer, I want the pipeline to automatically create a new branch, commit the Markdown file, and open a Pull Request for human review.
*   **Story 2.6:** As the librarian, I want a command-line script to manually trigger the curation process for a specific URL.
*   **Story 2.7:** As the librarian, I want the manual submission script to automatically detect the content type (e.g., blog post vs. research paper) and provide an option to override it.
