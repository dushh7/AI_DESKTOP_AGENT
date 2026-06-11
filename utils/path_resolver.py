import os


def get_desktop_path():
    return os.path.join(
        os.path.expanduser("~"),
        "OneDrive",
        "Desktop"
    )


def resolve_file_path(text: str):

    text = text.strip()

    desktop = get_desktop_path()

    # If full path already given
    if ":" in text or text.startswith("/"):
        return text

    # Extract filename if present
    words = text.split()

    for w in words:
        if "." in w:
            return os.path.join(desktop, w)

    # fallback → assume txt file
    cleaned = text.lower()
    cleaned = cleaned.replace("open", "")
    cleaned = cleaned.replace("file", "")
    cleaned = cleaned.replace("the", "")
    cleaned = cleaned.strip().replace('"', "")

    if not cleaned:
        cleaned = "file.txt"

    if not cleaned.endswith(".txt"):
        cleaned += ".txt"

    return os.path.join(desktop, cleaned)