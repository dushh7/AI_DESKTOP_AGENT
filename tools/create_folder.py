from pathlib import Path
import os


def create_folder(folder_path: str):
    try:

        # Normalize path
        path = Path(folder_path)

        # If only folder name is given (no path), create in current directory safety fallback
        if not str(path).strip():
            return "Invalid folder name provided."

        # Ensure folder creation
        path.mkdir(parents=True, exist_ok=True)

        return f"Folder created successfully:\n{str(path)}"

    except PermissionError:
        return f"Permission denied: {folder_path}"

    except FileNotFoundError:
        return f"Invalid path: {folder_path}"

    except Exception as e:
        return f"Error creating folder: {str(e)}"