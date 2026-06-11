from docx import Document


def read_docx(file_path: str) -> str:
    """
    Extract text from DOCX file.
    """

    try:

        doc = Document(file_path)

        text = []

        for paragraph in doc.paragraphs:
            text.append(paragraph.text)

        return "\n".join(text)

    except Exception as e:
        return f"Error reading DOCX: {str(e)}"