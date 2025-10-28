# AI Usage in the Quality Share Pipeline

This document describes how Artificial Intelligence (AI) is used in the Quality Share curation pipeline.

The pipeline leverages AI, specifically OpenAI's GPT model, to automate several key tasks in the process of curating and publishing articles.

## AI-Powered Workflow

The AI-powered workflow consists of the following steps:

1.  **Content Extraction:** The system first extracts the main content from a given article URL.

2.  **AI-Powered Analysis (OpenAI):** The extracted text is then sent to an AI model to perform three distinct tasks:
    *   **Summarization:** It generates a concise summary of the article.
    *   **Tagging:** It generates relevant keywords or tags that categorize the article's content.
    *   **Content Classification:** It automatically determines the type of content (e.g., `BLOG_POST`, `RESEARCH_PAPER`, `ROOT_CAUSE_ANALYSIS`).

3.  **Content Creation:** Finally, the AI-generated summary, tags, and classification are used to create a new Markdown file, which is then added to the website as a new article.

This automation helps to streamline the content curation process and ensures that the articles on the Quality Share website are well-summarized and categorized.
