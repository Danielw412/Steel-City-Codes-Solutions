"""Rock Paper Scissors solution using a dictionary of winning matchups."""

import random


choices = ["rock", "paper", "scissors"]
shortcuts = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
}

# Each key beats the value next to it.
beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def normalize_choice(text):
    """Convert shortcuts such as r, p, and s into full words."""
    text = text.strip().lower()

    if text in shortcuts:
        return shortcuts[text]

    return text


def main():
    score = {"wins": 0, "losses": 0, "ties": 0}

    print("Rock Paper Scissors")
    print("You can type rock, paper, scissors, r, p, or s.")

    while True:
        user_choice = normalize_choice(input("Your choice: "))

        if user_choice not in choices:
            print("That is not a valid choice.")
            continue

        computer_choice = random.choice(choices)
        print("Computer chose", computer_choice + ".")

        if user_choice == computer_choice:
            print("Tie!")
            score["ties"] += 1
        elif beats[user_choice] == computer_choice:
            print("You win!")
            score["wins"] += 1
        else:
            print("You lose.")
            score["losses"] += 1

        print("Score:", score)

        again = input("Play another round? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            break

    print("Final score:", score)


if __name__ == "__main__":
    main()
