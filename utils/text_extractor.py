import os
from utils.pdf_reader import read_pdf
from utils.docx_reader import read_docx


def extract_text(file_path):

    try:

        if not os.path.exists(file_path):
            return "File not found."

        ext = file_path.lower().split(".")[-1]

        if ext == "txt":
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()

        elif ext == "pdf":
            return read_pdf(file_path)

        elif ext == "docx":
            return read_docx(file_path)

        else:
            return "Unsupported file type"

    except Exception as e:
        return f"Error: {str(e)}"