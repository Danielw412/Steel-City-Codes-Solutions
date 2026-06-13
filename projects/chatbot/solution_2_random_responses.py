"""Chatbot solution that randomly chooses from several responses."""

import random


def contains_topic(message, topic):
    """Return True for a topic or a simple plural version of that topic."""
    return topic in message or topic + "s" in message


def main():
    print("Hello! I am a chatbot with a few random replies.")
    print("Try asking about python, bear, game, or food.")
    print("Type bye to exit.")

    while True:
        message = input("You: ").strip().lower()

        if message == "":
            print("Bot:", random.choice(["I need words to answer.", "Please type a message."]))
            continue

        if message in ["bye", "quit", "exit"]:
            print("Bot: Goodbye!")
            break

        if "hello" in message or "hi" in message:
            responses = ["Hello!", "Hi there!", "Nice to chat with you!"]
        elif contains_topic(message, "python"):
            responses = [
                "Python uses indentation to organize code.",
                "Python is often used for games, data, and websites.",
                "Python is a great first programming language.",
            ]
        elif contains_topic(message, "bear"):
            responses = [
                "Bears can be very powerful animals.",
                "Some bears hibernate during cold months.",
                "Bears can live in forests, mountains, and icy places.",
            ]
        elif contains_topic(message, "game"):
            responses = [
                "Games are a fun way to practice loops.",
                "A game often needs input, rules, and score tracking.",
                "Random numbers can make games more interesting.",
            ]
        elif contains_topic(message, "food"):
            responses = [
                "Food is a popular chatbot topic.",
                "I do not eat, but I can talk about snacks.",
                "Pizza is a classic coding-night food.",
            ]
        else:
            responses = ["Try python, bear, game, or food."]

        print("Bot:", random.choice(responses))


if __name__ == "__main__":
    main()
