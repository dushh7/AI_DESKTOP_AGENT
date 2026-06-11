import os
from utils.text_extractor import extract_text


def read_file(file_path: str):

    try:

        # Normalize path
        path = os.path.expanduser(file_path.strip())

        # Check if file exists
        if not os.path.exists(path):
            return f"File not found:\n{path}"

        # Extract text safely
        text = extract_text(path)

        if not text:
            return "File is empty or unsupported format."

        # Limit huge outputs (prevents Streamlit crash)
        if len(text) > 20000:
            text = text[:20000] + "\n\n... (truncated)"

        return text

    except PermissionError:
        return f"Permission denied: {file_path}"

    except Exception as e:
        return f"Error reading file: {str(e)}"