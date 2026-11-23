"""Magic 8 Ball solution that groups answers by mood."""

import random


response_groups = {
    "positive": [
        "Absolutely.",
        "Yes, that sounds right.",
        "The future looks bright.",
    ],
    "neutral": [
        "Maybe.",
        "Try asking again later.",
        "It could go either way.",
    ],
    "negative": [
        "No.",
        "I would not expect it.",
        "The chances are low.",
    ],
}


def get_all_responses():
    """Build one list that contains every response from every group."""
    all_responses = []

    for group in response_groups.values():
        for response in group:
            all_responses.append(response)

    return all_responses


def main():
    responses = get_all_responses()
    question_count = 0

    print("Magic 8 Ball is ready.")
    print("Type stop when you are finished.")

    while True:
        question = input("Question: ").strip()

        if question.lower() in ["stop", "quit", "exit"]:
            print("You asked", question_count, "question(s).")
            print("See you next time!")
            break

        if question == "":
            print("A blank question cannot be answered.")
            continue

        question_count += 1
        print(random.choice(responses))


if __name__ == "__main__":
    main()
