from pathlib import Path
import os


def create_file(file_path, content=""):
    try:

        # Normalize Windows path
        path = Path(file_path)

        # Ensure parent folders exist
        path.parent.mkdir(parents=True, exist_ok=True)

        # Ensure file has valid extension (optional safety)
        if path.suffix == "":
            path = Path(str(path) + ".txt")

        # Write file
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"File created successfully:\n{str(path)}"

    except PermissionError:
        return f"Permission denied: {file_path}"

    except Exception as e:
        return f"Error creating file: {str(e)}"