import unittest
from datetime import datetime
from markdown_creator import create_markdown_content
from content_classifier import ContentType

class TestMarkdownCreator(unittest.TestCase):

    def test_create_markdown_content(self):
        title = "Test Article Title"
        link = "http://example.com/test-article"
        summary = "This is a concise summary of the test article."
        tags = ["tag1", "tag2", "tag3"]
        published_date = datetime(2025, 10, 26, 10, 0, 0)
        content_type = ContentType.BLOG_POST.value

        expected_markdown = """
---
title: "Test Article Title"
date: 2025-10-26T10:00:00
link: "http://example.com/test-article"
summary: "This is a concise summary of the test article."
tags:
  - tag1
  - tag2
  - tag3
categories:
  - BLOG_POST
---

"""

        markdown_content = create_markdown_content(title, link, summary, tags, published_date, content_type)
        self.assertEqual(markdown_content, expected_markdown)

    def test_create_markdown_content_no_tags(self):
        title = "Test Article Title"
        link = "http://example.com/test-article"
        summary = "This is a concise summary of the test article."
        tags = []
        published_date = datetime(2025, 10, 26, 10, 0, 0)
        content_type = ContentType.RESEARCH_PAPER.value

        expected_markdown = """
---
title: "Test Article Title"
date: 2025-10-26T10:00:00
link: "http://example.com/test-article"
summary: "This is a concise summary of the test article."
tags:
categories:
  - RESEARCH_PAPER
---

"""

        markdown_content = create_markdown_content(title, link, summary, tags, published_date, content_type)
        self.assertEqual(markdown_content, expected_markdown)

if __name__ == '__main__':
    unittest.main()
