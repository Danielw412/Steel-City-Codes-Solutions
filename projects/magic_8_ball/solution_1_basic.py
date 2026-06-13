"""Magic 8 Ball solution using one simple loop."""

import random


responses = [
    "Yes, definitely!",
    "It is very likely.",
    "You can count on it.",
    "Ask again later.",
    "I am not sure yet.",
    "The answer is unclear.",
    "Probably not.",
    "Do not count on it.",
    "Very doubtful.",
]

print("Welcome to Magic 8 Ball!")
print("Ask a yes/no question, or type quit to stop.")

while True:
    question = input("Question: ").strip()

    if question.lower() in ["quit", "q", "exit"]:
        print("Thanks for playing!")
        break

    if question == "":
        print("Please type a question first.")
    else:
        answer = random.choice(responses)
        print("Magic 8 Ball says:", answer)
