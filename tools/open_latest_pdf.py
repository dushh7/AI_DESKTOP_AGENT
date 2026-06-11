import os
from pathlib import Path

from tools.open_file import open_file


def open_latest_pdf():

    folders = [
        Path.home() / "Desktop",
        Path.home() / "Downloads",
        Path.home() / "Documents",
        Path.home() / "OneDrive" / "Desktop"
    ]

    pdf_files = []

    for folder in folders:

        if folder.exists():

            for root, dirs, files in os.walk(folder):

                for file in files:

                    if file.lower().endswith(".pdf"):

                        full_path = os.path.join(root, file)

                        pdf_files.append(full_path)

    if not pdf_files:

        return "No PDF files found."

    latest_pdf = max(
        pdf_files,
        key=os.path.getmtime
    )

    open_file(latest_pdf)

    return f"Opened latest PDF:\n{latest_pdf}"