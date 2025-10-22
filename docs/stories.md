# Product Backlog

This document contains the user stories for the Quality Share project, organized by epic.

---

## Epic 1: Project Foundation & Setup

*   **Story 1.1:** As the project owner, I want the `source-tree` directory structure created in the repository, so that we have a clean and organized codebase.
    *   **Status:** Complete
*   **Story 1.2:** As a developer, I want a new Python project initialized with Poetry in the `pipeline` directory, so that I can start developing the AI Curation Pipeline.
    *   **Status:** Complete
*   **Story 1.3:** As the project owner, I want a basic Hugo site initialized in the `site` directory, so that we have a starting point for the website.
    *   **Status:** Complete
*   **Story 1.4:** As a developer, I want a basic CI/CD pipeline that automatically builds and deploys the Hugo site to GitHub Pages on every push to the `main` branch.
    *   **Status:** Complete
*   **Story 1.5:** As a developer, I want a basic testing workflow that runs `pytest` on every Pull Request to ensure code quality, with a target of 80% test coverage for the Python pipeline.
    *   **Status:** Complete
*   **Story 1.6:** As a project owner, I want to ensure that the implementation of the project is consistent with the architectural decisions and requirements documented in the `docs` directory, so that we have a high-quality and maintainable codebase.
    *   **Status:** Complete

---

## Epic 2: AI Curation Pipeline (MVP)

*   **Story 2.1:** As a developer, I want the pipeline to fetch the latest articles from a list of RSS feeds, so that we have a source of content to process.
    *   **Status:** Complete
*   **Story 2.2:** As a developer, I want the pipeline to check a SQLite database of visited URLs before processing an article, so that we don't create duplicate content.
    *   **Status:** Complete
*   **Story 2.3a:** As a developer, I want a function that can take a URL and extract the clean, main body of text from the article, stripping away boilerplate like headers, footers, and ads.
    *   **Status:** Complete
*   **Story 2.3b:** As a developer, I want a function that can take the extracted text and send it to an LLM to generate a concise summary.
    *   **Status:** Complete
*   **Story 2.3c:** As a developer, I want a function that can take the extracted text and send it to an LLM to generate a list of relevant tags.
    *   **Status:** Complete
*   **Story 2.4:** As a developer, I want the pipeline to create a new Markdown file with the processed content (title, summary, tags, etc.) formatted as front matter.
    *   **Status:** Complete
*   **Story 2.5:** As a developer, I want the pipeline to automatically create a new branch, commit the Markdown file, and open a Pull Request for human review.
    *   **Status:** Complete
*   **Story 2.6:** As the librarian, I want a command-line script to manually trigger the curation process for a specific URL.
    *   **Status:** Complete
*   **Story 2.7:** As the librarian, I want the manual submission script to automatically detect the content type (e.g., blog post vs. research paper) and provide an option to override it.
    *   **Status:** Complete
*   **Story 2.8: Generate Hugo Data File**
    *   As a developer, I want the pipeline to generate a `site/data/articles.json` file from the `published_content` table in the SQLite database, so that Hugo can easily access the curated article data.
    *   **Status:** Complete
*   **Story 2.9:** As a developer, I want to configure the AI Curation Pipeline to run on a recurring schedule using GitHub Actions, so that new content is discovered and processed automatically without manual intervention.
    *   **Status:** Complete

*   **Story 2.10:** As a developer, I want the AI Curation Pipeline to check for existing open Pull Requests for an article before creating a new one, so that duplicate Pull Requests are avoided.
    *   **Status:** To Do

*   **Story 2.11:** As a librarian, I want to trigger the manual article addition process via a GitHub Action, so that I can securely provide article URLs and content types without handling API tokens locally.
    *   **Status:** Complete

---

## Epic 3: Website & Content Display (MVP)

*   **Story 3.1:** As a project owner, I want the Hugo site to use the Ananke theme, so that we have a consistent and accessible visual design.
    *   **Status:** Complete
*   **Story 3.2:** As a visitor, I want to see a list of curated articles on the homepage, so that I can easily discover new content.
    *   **Status:** Complete
*   **Story 3.3:** As a visitor, I want to be able to click on an article and see its full content (summary, tags, link to original), so that I can read more about it.
    *   **Status:** Complete
*   **Story 3.4:** As a visitor, I want to access an "About" page that explains the project's mission and philosophy, so that I can understand what Quality Share is about.
    *   **Status:** Complete
*   **Story 3.5:** As a visitor, I want to see a "View on GitHub" link in the site's footer, so that I can easily find the project's source code.
    *   **Status:** Complete
*   **Story 3.6:** As a visitor, I want the website to be usable and readable on different screen sizes (desktop, tablet, mobile), so that I can access content from any device.
    *   **Status:** Complete
*   **Story 3.7:** As a project owner, I want to add my LinkedIn profile link with a logo in the site's footer, so that visitors can easily connect with me.
    *   **Status:** Complete
*   **Story 3.8:** As a visitor, I want to be able to view the project's architectural decisions, so that I can understand the rationale behind the system's design.
    *   **Status:** Complete
*   **Story 3.9:** As a visitor, I want to be able to access a glossary of terms, so that I can understand the terminology used in the project.
    *   **Status:** Complete
*   **Story 3.10:** As a visitor, I want to see separate menus for "research papers", "blogs", and "root cause analysis", so that I can easily filter and browse the content by type.
    *   **Status:** Complete
*   **Story 3.11:** As a user, I want to be able to provide feedback on whether an article was useful, so that I can help improve the quality of the curated content.
    *   **Status:** To Do
*   **Story 3.12:** As a user, I want to be able to navigate to a dedicated page for each individual article, so that I can read the article's summary and share a direct link to it.
    *   **Status:** Complete
*   **Story 3.13:** As a returning visitor, I want to easily identify newly added articles, even if they are older, so that I don't miss any new content. This will be implemented with a "New" badge next to articles curated in the last 7 days.
    *   **Status:** To Do
*   **Story 3.14:** As a project owner, I want to populate the privacy policy page with detailed information, so that users understand how their data is handled.
    *   **Status:** To Do

*   **Story 3.15:** As a project owner, I want to evaluate alternative Hugo themes, so that I can ensure the website has the most appealing and functional visual design.
    *   **Status:** To Do

---

## Epic 4: NFRs & Analytics

*   **Story 4.1:** As a project owner, I want to integrate a secrets scanning tool into the CI/CD workflow, so that we can prevent accidental commitment of secrets.
    *   **Status:** Complete
*   **Story 4.2:** As a developer, I want to receive email notifications for any CI/CD pipeline failures, so that I can promptly investigate and resolve issues using GitHub's built-in notification features.
    *   **Status:** Complete
*   **Story 4.3:** As a project owner, I want to implement Google Analytics with a cookie consent banner, so that we can gather website usage data while respecting user privacy.
    *   **Status:** Complete
*   **Story 4.4:** As a project owner, I want to enable `Dependabot` to automatically scan our. dependencies for vulnerabilities, so that we can keep our project secure.
    *   **Status:** Complete
*   **Story 4.5:** As a project owner, I want to configure all the necessary secrets (e.g., `OPENAI_API_KEY`, `GOOGLE_ANALYTICS_MEASUREMENT_ID`) in the GitHub repository, so that the CI/CD pipelines can run successfully.
    *   **Status:** Complete

---

## Epic 5: Future Enhancements

*   **Story 5.1:** As a developer, I want to mock OpenAI API calls in unit tests, so that I can avoid incurring costs and ensure test stability without external dependencies.
    *   **Status:** To Do