from langchain_ollama import ChatOllama
from utils.text_extractor import extract_text


llm = ChatOllama(
    model="llama3",
    temperature=0
)


def summarize_file(file_path):

    try:

        text = extract_text(file_path)

        if not text:
            return "No text found."

        text = text[:5000]

        prompt = f"""
Summarize the following document clearly and concisely.

DOCUMENT:
{text}
"""

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return f"Error: {str(e)}"