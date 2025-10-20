import unittest
from content_classifier import classify_content, ContentType

class TestContentClassifier(unittest.TestCase):

    def test_classify_research_paper_by_url(self):
        url = "https://arxiv.org/abs/2301.00001"
        text_content = "Some text content."
        self.assertEqual(classify_content(url, text_content), ContentType.RESEARCH_PAPER)

    def test_classify_research_paper_by_doi(self):
        url = "https://example.com/blog/post"
        text_content = "This article discusses a new method. DOI: 10.1234/some.doi.123"
        self.assertEqual(classify_content(url, text_content), ContentType.RESEARCH_PAPER)

    def test_classify_blog_post(self):
        url = "https://mytechblog.com/post/latest"
        text_content = "This is a blog post about software development."
        self.assertEqual(classify_content(url, text_content), ContentType.BLOG_POST)

    def test_classify_unknown_type(self):
        url = "https://unknownsite.com/page"
        text_content = "Some generic content without specific indicators."
        self.assertEqual(classify_content(url, text_content), ContentType.BLOG_POST) # Defaults to BLOG_POST

if __name__ == '__main__':
    unittest.main()
