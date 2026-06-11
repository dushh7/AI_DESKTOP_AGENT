import os
from langchain_ollama import ChatOllama

from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

from tools.create_folder import create_folder
from tools.create_file import create_file
from tools.read_file import read_file
from tools.search_file import search_file
from tools.delete_file import delete_file
from tools.open_file import open_file
from tools.summarize_file import summarize_file
from tools.open_latest_pdf import open_latest_pdf


# ==========================
# LLM
# ==========================
llm = ChatOllama(
    model="llama3",
    temperature=0
)


# ==========================
# Desktop Path Helper
# ==========================
def get_desktop_path():
    import os

    onedrive = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

    if os.path.exists(onedrive):
        return onedrive

    return os.path.join(os.path.expanduser("~"), "Desktop")


# ==========================
# TOOL WRAPPERS
# ==========================

def create_folder_tool(path: str):
    if "desktop" in path.lower():
        path = os.path.join(get_desktop_path(), path.replace("desktop", "").strip())
    return create_folder(path)


def create_file_tool(path: str):
    if "desktop" in path.lower():
        filename = path.replace("desktop", "").strip()
        if not filename.endswith(".txt"):
            filename += ".txt"
        path = os.path.join(get_desktop_path(), filename)

    return create_file(path, "")


def search_file_tool(filename: str):
    return "\n".join(search_file(r"C:\\Users", filename)[:20])


def open_latest_pdf_tool(_):
    return open_latest_pdf()


# ==========================
# LANGCHAIN TOOLS
# ==========================
tools = [

    Tool(
        name="CreateFolder",
        func=create_folder_tool,
        description="Create a folder. Input: full path or folder name."
    ),

    Tool(
        name="CreateFile",
        func=create_file_tool,
        description="Create a text file. Input: filename or full path."
    ),

    Tool(
        name="ReadFile",
        func=read_file,
        description="Read any text, PDF, or DOCX file."
    ),

    Tool(
        name="SearchFile",
        func=search_file_tool,
        description="Search files by name in system."
    ),

    Tool(
        name="DeleteFile",
        func=delete_file,
        description="Delete a file by full path."
    ),

    Tool(
        name="OpenFile",
        func=open_file,
        description="Open a file using system default app."
    ),

    Tool(
        name="SummarizeFile",
        func=summarize_file,
        description="Summarize documents (PDF, DOCX, TXT)."
    ),

    Tool(
        name="OpenLatestPDF",
        func=open_latest_pdf_tool,
        description="Open the most recently modified PDF file."
    )
]


# ==========================
# AGENT
# ==========================
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


# ==========================
# MAIN FUNCTION
# ==========================
def run_agent(query: str):
    try:
        response = agent.invoke({"input": query})
        return response["output"]

    except Exception as e:
        return f"Error: {str(e)}"