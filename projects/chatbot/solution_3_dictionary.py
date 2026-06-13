"""Chatbot solution using a dictionary of topics and responses."""

import random


topics = {
    "python": [
        "Python code can be short and readable.",
        "Python lets you build terminal programs with input and print.",
    ],
    "bear": [
        "Bears have an excellent sense of smell.",
        "A bear can be a good example topic for plural keyword checks.",
    ],
    "music": [
        "Music has rhythm, and programs have flow.",
        "A playlist can make practice more enjoyable.",
    ],
    "weather": [
        "Weather changes often, just like program variables.",
        "I hope the weather is nice where you are.",
    ],
}


def clean_words(message):
    """Split a message into simple lowercase words."""
    punctuation = ".,!?;:"
    message = message.lower()

    for mark in punctuation:
        message = message.replace(mark, " ")

    return message.split()


def find_topic(words):
    """Find the first known topic in the user's words."""
    for topic in topics:
        if topic in words or topic + "s" in words:
            return topic

    return None


def main():
    print("Hello! I am a dictionary chatbot.")
    print("Known topics:", ", ".join(topics.keys()))
    print("Type bye to exit.")

    while True:
        message = input("You: ").strip()

        if message == "":
            print("Bot: Please type something.")
            continue

        if message.lower() in ["bye", "quit", "exit"]:
            print("Bot: Goodbye!")
            break

        words = clean_words(message)

        if "hello" in words or "hi" in words:
            print("Bot: Hello!")
            continue

        topic = find_topic(words)

        if topic is None:
            print("Bot: I can talk about", ", ".join(topics.keys()) + ".")
        else:
            print("Bot:", random.choice(topics[topic]))


if __name__ == "__main__":
    main()
