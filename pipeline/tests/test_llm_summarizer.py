import unittest
import os
from unittest.mock import patch, MagicMock
from llm_summarizer import summarize_text, generate_tags

class TestLlmSummarizer(unittest.TestCase):

    @patch('llm_summarizer.load_summarize_chain')
    def test_summarize_text_success(self, mock_load_summarize_chain):
        # Mock the load_summarize_chain function to return a mock chain
        mock_chain = MagicMock()
        mock_load_summarize_chain.return_value = mock_chain

        # Mock the run method of the chain
        mock_chain.run.return_value = "This is a concise summary."

        # Set a dummy API key for the test
        with patch.dict('os.environ', {'OPENAI_API_KEY': 'test_key'}):
            # Call the function
            summary = summarize_text("This is a long text that needs to be summarized.")

            # Assert the results
            self.assertEqual(summary, "This is a concise summary.")
            mock_load_summarize_chain.assert_called_once()
            mock_chain.run.assert_called_once()

    def test_summarize_text_no_api_key(self):
        # Ensure API key is not set
        if 'OPENAI_API_KEY' in os.environ:
            del os.environ['OPENAI_API_KEY']

        with self.assertRaises(ValueError) as cm:
            summarize_text("Some text.")
        self.assertEqual(str(cm.exception), "OPENAI_API_KEY environment variable not set.")

    @patch('langchain_core.prompts.ChatPromptTemplate.from_messages')
    @patch('langchain_core.language_models.base.BaseLanguageModel.invoke')
    def test_generate_tags_success(self, mock_invoke, mock_from_messages):
        # Mock the from_messages method to return a mock prompt
        mock_prompt = MagicMock()
        mock_from_messages.return_value = mock_prompt

        # Mock the invoke method of the chain
        mock_invoke.return_value.content = "tag1, tag2, tag3"

        # Set a dummy API key for the test
        with patch.dict('os.environ', {'OPENAI_API_KEY': 'test_key'}):
            # Call the function
            tags = generate_tags("This is a text to extract tags from.")

            # Assert the results
            self.assertEqual(tags, ["tag1", "tag2", "tag3"])
            mock_from_messages.assert_called_once()
            mock_invoke.assert_called_once()

    def test_generate_tags_no_api_key(self):
        # Ensure API key is not set
        if 'OPENAI_API_KEY' in os.environ:
            del os.environ['OPENAI_API_KEY']

        with self.assertRaises(ValueError) as cm:
            generate_tags("Some text.")
        self.assertEqual(str(cm.exception), "OPENAI_API_KEY environment variable not set.")

if __name__ == '__main__':
    unittest.main()
