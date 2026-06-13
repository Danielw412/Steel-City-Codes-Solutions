"""Hangman solution using one main game loop."""

import random


words = ["python", "planet", "school", "window", "yellow", "bridge"]

print("Hangman")

while True:
    word = random.choice(words)
    guessed_letters = []
    wrong_letters = []
    attempts_left = 6

    while True:
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print()
        print("Word:", display.strip())
        print("Guessed letters:", " ".join(guessed_letters + wrong_letters))
        print("Attempts left:", attempts_left)

        if "_" not in display:
            print("You guessed the word!")
            break

        if attempts_left == 0:
            print("You ran out of attempts. The word was", word + ".")
            break

        guess = input("Guess one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            wrong_letters.append(guess)
            attempts_left -= 1
            print("That letter is not in the word.")

    again = input("Play again? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("Thanks for playing!")
        break
