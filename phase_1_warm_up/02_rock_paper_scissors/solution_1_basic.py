"""Rock Paper Scissors solution with three rounds and score tracking."""

import random


choices = ["rock", "paper", "scissors"]
wins = 0
losses = 0
ties = 0

print("Rock Paper Scissors")
print("You will play 3 rounds.")

for round_number in range(1, 4):
    print()
    print("Round", round_number)

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if user_choice in choices:
            break

        print("Invalid choice. Please try again.")

    computer_choice = random.choice(choices)
    print("Computer chose", computer_choice + ".")

    if user_choice == computer_choice:
        print("Tie!")
        ties += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        wins += 1
    else:
        print("You lose.")
        losses += 1

print()
print("Final score")
print("Wins:", wins)
print("Losses:", losses)
print("Ties:", ties)
