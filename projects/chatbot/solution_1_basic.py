"""Chatbot solution using basic if and elif statements."""


print("Hello! I am a Python chatbot.")
print("Ask me about python, bears, music, or school.")
print("Type bye to exit.")

while True:
    message = input("You: ").strip().lower()

    if message == "":
        print("Bot: Please type a message.")
    elif message in ["bye", "quit", "exit"]:
        print("Bot: Goodbye!")
        break
    elif "hello" in message or "hi" in message:
        print("Bot: Hi there!")
    elif "python" in message:
        print("Bot: Python is a friendly language for learning programming.")
    elif "bear" in message or "bears" in message:
        print("Bot: Bears are strong mammals. Some eat berries, fish, and insects.")
    elif "music" in message:
        print("Bot: Music can help make practice time more fun.")
    elif "school" in message:
        print("Bot: School is a good place to practice asking questions.")
    else:
        print("Bot: I know about python, bears, music, and school.")
