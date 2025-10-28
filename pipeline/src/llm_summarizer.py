import os
from langchain_openai import ChatOpenAI
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the LLM at module level
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

def summarize_text(text: str) -> str:
    """Generates a concise summary of the given text using an LLM, handling long texts.

    Args:
        text: The text to summarize.

    Returns:
        A concise summary of the text.
    """
    # Ensure OpenAI API key is set as an environment variable
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    # For long texts, we need to split them into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=200)
    docs = text_splitter.create_documents([text])

    # Use the map_reduce chain to handle long texts
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)

    return summary

def generate_tags(text: str) -> list[str]:
    """Generates a list of relevant tags from the given text using an LLM.

    Args:
        text: The text to extract tags from.

    Returns:
        A list of relevant tags.
    """
    # Define the tagging prompt at module level
    tagging_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that extracts relevant keywords and tags from text. Return tags as a comma-separated list."),
        ("user", "Extract tags from the following text: {text}"),
    ])

    # Create the tagging chain at module level
    tagging_chain = tagging_prompt | llm | StrOutputParser()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    # For long texts, we can't process the whole text at once.
    # We will truncate the text to fit within the context window.
    # This is not ideal, but it's a simple solution for now.
    max_text_length = 15000 # A bit less than the context window
    if len(text) > max_text_length:
        text = text[:max_text_length]


    tags_str = tagging_chain.invoke({"text": text})
    return [tag.strip() for tag in tags_str.split(',') if tag.strip()]