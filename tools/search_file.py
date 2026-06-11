import os
import re


def clean_query(text: str) -> str:
    """
    Extract meaningful search keyword from natural language input
    """

    text = text.lower().strip()

    # remove common AI instruction words
    remove_words = [
        "search", "file", "for", "find", "open", "in", "my", "system",
        "desktop", "downloads", "documents", "folder"
    ]

    for w in remove_words:
        text = text.replace(w, "")

    # extract quoted text first (highest priority)
    quoted = re.findall(r'"(.*?)"|\'(.*?)\'', text)
    if quoted:
        return quoted[0][0] or quoted[0][1]

    # clean extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def search_file(root_directory, filename):

    matches = []

    try:
        filename = clean_query(filename)

        if not filename:
            return []

        filename_words = filename.lower().split()

        for root, dirs, files in os.walk(root_directory):

            for file in files:

                file_lower = file.lower()

                # SMART MATCHING (IMPORTANT FIX)
                if any(word in file_lower for word in filename_words):

                    matches.append(os.path.join(root, file))

        return matches

    except Exception as e:
        return [f"Error: {str(e)}"]