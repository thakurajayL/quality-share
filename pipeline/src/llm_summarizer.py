import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the LLM at module level
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Define the summarization prompt at module level
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that summarizes text concisely."),
    ("user", "Summarize the following text: {text}"),
])

# Create the summarization chain at module level
summarization_chain = prompt | llm | StrOutputParser()

def summarize_text(text: str) -> str:
    """Generates a concise summary of the given text using an LLM.

    Args:
        text: The text to summarize.

    Returns:
        A concise summary of the text.
    """
    # Ensure OpenAI API key is set as an environment variable
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    # Invoke the chain to get the summary
    summary = summarization_chain.invoke({"text": text})

    return summary

# Define the tagging prompt at module level
tagging_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that extracts relevant keywords and tags from text. Return tags as a comma-separated list."),
    ("user", "Extract tags from the following text: {text}"),
])

# Create the tagging chain at module level
tagging_chain = tagging_prompt | llm | StrOutputParser()

def generate_tags(text: str) -> list[str]:
    """Generates a list of relevant tags from the given text using an LLM.

    Args:
        text: The text to extract tags from.

    Returns:
        A list of relevant tags.
    """
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    tags_str = tagging_chain.invoke({"text": text})
    return [tag.strip() for tag in tags_str.split(',') if tag.strip()]