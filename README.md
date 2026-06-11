# 🤖 AI Desktop Agent

AI Desktop Agent is an intelligent desktop automation application built using Python, LangGraph, LangChain, Ollama, Llama 3, and Streamlit.

The project allows users to interact with their computer using natural language commands and automate common desktop operations.

The system understands user instructions and performs actions such as creating files, creating folders, opening files, reading document contents, summarizing documents, and opening the latest PDF automatically.

This project demonstrates how Large Language Models (LLMs) can be integrated with desktop automation to create an interactive AI assistant that performs real system operations locally.

---

# 🚀 Features

- Create files anywhere in the system
- Create folders anywhere in the system
- Open files using default operating system applications
- Read TXT, PDF, and DOCX documents
- Summarize document content using AI
- Automatically open the latest PDF
- Process natural language commands
- Execute desktop automation locally
- Interactive Streamlit interface
- Workflow orchestration using LangGraph
- Local AI execution using Ollama and Llama 3

---

# 🛠 Technologies Used

## Python
Main programming language used for desktop automation and application development.

## Streamlit
Used to create the interactive web interface.

## LangGraph
Used to design and manage AI workflow execution.

## LangChain
Used to connect the language model with custom automation tools.

## Ollama
Runs local language models without external APIs.

## Llama 3
Provides natural language understanding and response generation.

## OS Module
Handles operating system interaction and file operations.

## Pathlib
Used for efficient path management.

## Regular Expressions (re)
Used for extracting filenames, folder names, and commands.

---

# 📂 Project Structure

```plaintext
AI_DESKTOP_AGENT/
│
├── app.py
│
├── agents/
│   └── langgraph_agent.py
│
├── tools/
│   ├── create_file.py
│   ├── create_folder.py
│   ├── read_file.py
│   ├── delete_file.py
│   ├── open_file.py
│   ├── summarize_file.py
│   └── open_latest_pdf.py
│
├── utils/
│   ├── text_extractor.py
│   └── path_resolver.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Workflow

### Step 1 — User Input

User enters a natural language command.

Example:

```text
Create file "Meeting Notes" in Desktop
```

---

### Step 2 — Intent Detection

LangGraph identifies the user request.

Supported actions:

- create_file
- create_folder
- open_file
- read_file
- summarize_file
- open_latest_pdf

---

### Step 3 — Path Resolution

Natural language is converted into a real system path.

Example:

```text
Desktop
↓
C:\Users\Username\OneDrive\Desktop
```

---

### Step 4 — Tool Execution

The system executes the selected desktop operation.

Examples:

- File Creation
- Folder Creation
- File Opening
- Document Reading
- Document Summarization

---

### Step 5 — Response

Execution result is displayed in Streamlit.

Example:

```text
File created successfully:
C:\Users\DUSHI\Desktop\Meeting Notes.txt
```

---

# 💬 Example Commands

## Create File

```text
Create file "Project Notes" in Desktop
```

## Create Folder

```text
Create folder "Internship Project" in Documents
```

## Open File

```text
Open "Resume.docx"
```

## Read File

```text
Read "Project Report.pdf"
```

## Summarize Document

```text
Summarize "Internship Report.docx"
```

## Open Latest PDF

```text
Open latest PDF
```

---

# 🔧 Installation

Clone Repository:

```bash
git clone <repository-url>
```

Move to Project:

```bash
cd AI_DESKTOP_AGENT
```

Create Virtual Environment:

```bash
python -m venv venv
```

Activate Environment:

```bash
venv\Scripts\activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Run Project

Start Ollama:

```bash
ollama run llama3
```

Run Streamlit:

```bash
streamlit run app.py
```

Open Browser:

```text
http://localhost:8501
```

---

# 📌 Objectives

- Build an AI-powered desktop assistant
- Automate desktop operations
- Integrate local LLMs
- Enable natural language interaction
- Develop an internship-level AI project

---

# 🔮 Future Enhancements

- Voice command support
- Autonomous workflows
- File editing
- Image understanding
- Cross-platform support
- Advanced AI actions

---

# 👨‍💻 Author

Developed by **Dushyan S**

AI & Python Internship Project

VCodeWonders