"""Hangman solution that includes word hints."""

import random


word_hints = {
    "python": "a programming language",
    "guitar": "a musical instrument",
    "jacket": "something you wear",
    "planet": "a large object in space",
    "cookie": "a sweet snack",
}


def choose_puzzle():
    """Choose a word and its hint."""
    word = random.choice(list(word_hints.keys()))
    return word, word_hints[word]


def show_word(word, guessed):
    """Return a display with letters and blanks."""
    pieces = []

    for letter in word:
        if letter in guessed:
            pieces.append(letter)
        else:
            pieces.append("_")

    return " ".join(pieces)


def read_guess(guessed):
    """Read a valid new letter."""
    while True:
        guess = input("Guess one letter: ").strip().lower()

        if len(guess) != 1:
            print("Enter one letter.")
        elif not guess.isalpha():
            print("Letters only, please.")
        elif guess in guessed:
            print("You already tried that letter.")
        else:
            return guess


def play_round():
    word, hint = choose_puzzle()
    guessed = []
    attempts_left = 6
    wrong_count = 0

    print("Hint:", hint)

    while True:
        print()
        print("Word:", show_word(word, guessed))
        print("Guessed:", " ".join(guessed))
        print("Attempts left:", attempts_left)

        if "_" not in show_word(word, guessed):
            print("You win! The word was", word + ".")
            return

        if attempts_left == 0:
            print("You lose. The word was", word + ".")
            return

        guess = read_guess(guessed)
        guessed.append(guess)

        if guess in word:
            print("Yes, that letter is in the word.")
        else:
            attempts_left -= 1
            wrong_count += 1
            print("No, that letter is not in the word.")

            if wrong_count == 3:
                print("Reminder hint:", hint)


def main():
    print("Hangman with Hints")

    while True:
        play_round()

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
