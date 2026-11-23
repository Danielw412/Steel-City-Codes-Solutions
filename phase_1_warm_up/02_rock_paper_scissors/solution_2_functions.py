"""Rock Paper Scissors solution using helper functions."""

import random


choices = ["rock", "paper", "scissors"]


def get_user_choice():
    """Ask until the user enters a valid choice."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if choice in choices:
            return choice

        print("Please enter rock, paper, or scissors.")


def get_computer_choice():
    """Return a random computer choice."""
    return random.choice(choices)


def get_result(user_choice, computer_choice):
    """Return win, lose, or tie for this round."""
    if user_choice == computer_choice:
        return "tie"

    if user_choice == "rock" and computer_choice == "scissors":
        return "win"

    if user_choice == "paper" and computer_choice == "rock":
        return "win"

    if user_choice == "scissors" and computer_choice == "paper":
        return "win"

    return "lose"


def main():
    print("Rock Paper Scissors")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = get_result(user_choice, computer_choice)

        print("Computer chose", computer_choice + ".")

        if result == "win":
            print("You win!")
        elif result == "lose":
            print("You lose.")
        else:
            print("Tie!")

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
