import os
import re
from typing import TypedDict

from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END

from tools.create_folder import create_folder
from tools.create_file import create_file
from tools.read_file import read_file
from tools.search_file import search_file
from tools.delete_file import delete_file
from tools.open_file import open_file
from tools.summarize_file import summarize_file
from tools.open_latest_pdf import open_latest_pdf


# =========================
# LLM
# =========================
llm = ChatOllama(model="llama3", temperature=0)


# =========================
# PATH RESOLVER (FIXED + SAFE)
# =========================
def get_base_dirs():
    home = os.path.expanduser("~")

    desktop = os.path.join(home, "OneDrive", "Desktop")
    if not os.path.exists(desktop):
        desktop = os.path.join(home, "Desktop")

    return {
        "desktop": desktop,
        "downloads": os.path.join(home, "Downloads"),
        "documents": os.path.join(home, "Documents"),
        "home": home
    }


def resolve_path(text: str) -> str:

    base = get_base_dirs()
    text_lower = text.lower()

    # 1. FULL PATH SUPPORT (BEST PRIORITY)
    match = re.search(r'([A-Za-z]:\\[^\s"\']+)', text)
    if match:
        return match.group(1)

    # 2. QUOTED NAME SUPPORT
    quoted = re.findall(r'"(.*?)"|\'(.*?)\'', text)
    if quoted:
        name = quoted[0][0] or quoted[0][1]
    else:
        name = text.split()[-1]

    # 3. LOCATION DETECTION
    if "desktop" in text_lower:
        return os.path.join(base["desktop"], name)

    if "downloads" in text_lower:
        return os.path.join(base["downloads"], name)

    if "documents" in text_lower:
        return os.path.join(base["documents"], name)

    return os.path.join(base["desktop"], name)


# =========================
# STATE
# =========================
class AgentState(TypedDict):
    input: str
    action: str
    result: str


# =========================
# ROUTER (FIXED PRIORITY LOGIC)
# =========================
def router(state: AgentState):

    text = state["input"].lower()

    # IMPORTANT: priority order (avoid conflicts)

    if "summarize" in text:
        return {"action": "summarize_file"}

    if "latest pdf" in text:
        return {"action": "open_latest_pdf"}

    if "create folder" in text:
        return {"action": "create_folder"}

    if "create file" in text:
        return {"action": "create_file"}

    if "search" in text:
        return {"action": "search_file"}

    if "delete" in text:
        return {"action": "delete_file"}

    if "open" in text:
        return {"action": "open_file"}

    if "read" in text:
        return {"action": "read_file"}

    return {"action": "chat"}


# =========================
# EXECUTOR (FULL FIXED LOGIC)
# =========================
def executor(state: AgentState):

    text = state["input"]
    action = state["action"]

    try:

        # ================= CREATE FOLDER =================
        if action == "create_folder":
            path = resolve_path(text)
            return {"result": create_folder(path)}

        # ================= CREATE FILE =================
        elif action == "create_file":
            path = resolve_path(text)

            if not path.endswith(".txt"):
                path += ".txt"

            return {"result": create_file(path, "")}

        # ================= SEARCH FILE (IMPROVED) =================
        elif action == "search_file":

            query = text.split()[-1]  # clean keyword

            roots = [
                get_base_dirs()["desktop"],
                get_base_dirs()["downloads"],
                get_base_dirs()["documents"]
            ]

            results = []
            for root in roots:
                if os.path.exists(root):
                    results.extend(search_file(root, query))

            if not results:
                return {"result": "No files found."}

            return {"result": "\n".join(results[:15])}

        # ================= DELETE =================
        elif action == "delete_file":
            path = resolve_path(text)
            return {"result": delete_file(path)}

        # ================= OPEN FILE =================
        elif action == "open_file":
            path = resolve_path(text)
            return {"result": open_file(path)}

        # ================= READ FILE =================
        elif action == "read_file":
            path = resolve_path(text)
            return {"result": read_file(path)}

        # ================= SUMMARIZE FILE =================
        elif action == "summarize_file":

            path = resolve_path(text)

            if not os.path.exists(path):
                return {"result": f"File not found: {path}"}

            content = read_file(path)

            summary = llm.invoke(
                f"Summarize this document:\n{content[:6000]}"
            ).content

            return {
                "result": f"File: {path}\n\nSummary:\n{summary}"
            }

        # ================= OPEN LATEST PDF =================
        elif action == "open_latest_pdf":
            return {"result": open_latest_pdf()}

        # ================= CHAT =================
        else:
            return {"result": llm.invoke(text).content}

    except Exception as e:
        return {"result": f"Error: {str(e)}"}


# =========================
# BUILD GRAPH
# =========================
graph = StateGraph(AgentState)

graph.add_node("router", router)
graph.add_node("executor", executor)

graph.set_entry_point("router")

graph.add_edge("router", "executor")
graph.add_edge("executor", END)

app = graph.compile()


# =========================
# RUN FUNCTION
# =========================
def run_agent(query: str):

    return app.invoke({
        "input": query,
        "action": "",
        "result": ""
    })["result"]