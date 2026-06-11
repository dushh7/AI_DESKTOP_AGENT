import shutil
from pathlib import Path


def move_file(source, destination):

    try:

        Path(destination).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.move(
            source,
            destination
        )

        return f"Moved:\n{source}\n\nTo:\n{destination}"

    except Exception as e:

        return f"Error: {str(e)}"