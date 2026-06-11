import os


def resolve_path(file_path: str):
    """
    Safe local resolver for Windows desktop agent
    """

    path = file_path.strip()

    # Expand user (~)
    path = os.path.expanduser(path)

    # If it's already absolute path, return as-is
    if os.path.isabs(path):
        return path

    # Otherwise assume it's a file in current directory
    return os.path.abspath(path)


def open_file(file_path: str):

    try:

        path = resolve_path(file_path)

        if not os.path.exists(path):
            return f"File not found:\n{path}"

        os.startfile(path)

        return f"Opened successfully:\n{path}"

    except PermissionError:
        return f"Permission denied:\n{file_path}"

    except Exception as e:
        return f"Error opening file: {str(e)}"