import unittest
import os
from unittest.mock import patch, MagicMock
from langchain_core.outputs import Generation
from llm_summarizer import summarize_text, summarization_chain

class TestLlmSummarizer(unittest.TestCase):

    @patch('llm_summarizer.summarization_chain')
    def test_summarize_text_success(self, mock_summarization_chain):
        # Mock the summarization chain's invoke method
        mock_summarization_chain.invoke.return_value = "This is a concise summary."

        # Set a dummy API key for the test
        with patch.dict('os.environ', {'OPENAI_API_KEY': 'test_key'}):
            # Call the function
            summary = summarize_text("This is a long text that needs to be summarized.")

            # Assert the results
            self.assertEqual(summary, "This is a concise summary.")
            mock_summarization_chain.invoke.assert_called_once_with({"text": "This is a long text that needs to be summarized."})

    @patch('llm_summarizer.ChatOpenAI')
    def test_summarize_text_no_api_key(self, mock_chat_openai):
        # Ensure API key is not set
        if 'OPENAI_API_KEY' in os.environ:
            del os.environ['OPENAI_API_KEY']

        with self.assertRaises(ValueError) as cm:
            summarize_text("Some text.")
        self.assertEqual(str(cm.exception), "OPENAI_API_KEY environment variable not set.")

if __name__ == '__main__':
    unittest.main()
