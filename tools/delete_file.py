import os


def delete_file(file_path):

    try:

        if os.path.exists(file_path):

            os.remove(file_path)

            return f"Deleted:\n{file_path}"

        return "File not found"

    except Exception as e:

        return f"Error: {str(e)}"