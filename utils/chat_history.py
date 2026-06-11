import json


HISTORY_FILE = "memory/chat_history.json"


def load_history():

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return []


def save_message(
    user,
    assistant
):

    history = load_history()

    history.append({
        "user": user,
        "assistant": assistant
    })

    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )