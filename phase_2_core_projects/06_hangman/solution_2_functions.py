"""Hangman solution organized with functions."""

import random


words = ["apple", "forest", "castle", "summer", "rocket", "pencil"]


def choose_word():
    """Choose a secret word."""
    return random.choice(words)


def make_display(word, correct_letters):
    """Build the visible word with blanks."""
    display_parts = []

    for letter in word:
        if letter in correct_letters:
            display_parts.append(letter)
        else:
            display_parts.append("_")

    return " ".join(display_parts)


def get_guess(all_guesses):
    """Ask for one new letter."""
    while True:
        guess = input("Guess one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please type exactly one letter.")
            continue

        if guess in all_guesses:
            print("You already guessed that letter.")
            continue

        return guess


def has_won(word, correct_letters):
    """Return True when every letter has been guessed."""
    for letter in word:
        if letter not in correct_letters:
            return False

    return True


def play_game():
    word = choose_word()
    correct_letters = []
    wrong_letters = []
    attempts_left = 6

    while attempts_left > 0:
        print()
        print("Word:", make_display(word, correct_letters))
        print("Wrong letters:", " ".join(wrong_letters))
        print("Attempts left:", attempts_left)

        if has_won(word, correct_letters):
            print("You win!")
            return

        guess = get_guess(correct_letters + wrong_letters)

        if guess in word:
            correct_letters.append(guess)
            print("Correct!")
        else:
            wrong_letters.append(guess)
            attempts_left -= 1
            print("Incorrect.")

    print("You lost. The word was", word + ".")


def main():
    print("Hangman")

    while True:
        play_game()
        again = input("Play again? (yes/no): ").strip().lower()

        if again not in ["yes", "y"]:
            break


if __name__ == "__main__":
    main()
