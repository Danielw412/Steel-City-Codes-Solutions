"""Magic 8 Ball solution organized with small functions."""

import random


def get_responses():
    """Return the list of possible Magic 8 Ball answers."""
    return [
        "Yes!",
        "Signs point to yes.",
        "Without a doubt.",
        "Maybe.",
        "Ask again soon.",
        "I need more time to think.",
        "No.",
        "My sources say no.",
        "That does not look likely.",
    ]


def wants_to_quit(text):
    """Return True when the user typed a quit command."""
    return text.lower() in ["quit", "q", "exit"]


def get_answer():
    """Choose and return one answer."""
    responses = get_responses()
    return random.choice(responses)


def main():
    print("Welcome to Magic 8 Ball!")
    print("Type quit when you are done.")

    while True:
        question = input("Ask a question: ").strip()

        if wants_to_quit(question):
            print("Goodbye!")
            break

        if question == "":
            print("Please ask a question.")
            continue

        print("Magic 8 Ball says:", get_answer())


if __name__ == "__main__":
    main()
