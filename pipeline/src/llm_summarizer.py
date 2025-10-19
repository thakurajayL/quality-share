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