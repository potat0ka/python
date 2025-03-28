#Rock, Paper, Scissors Game: Ask the user to enter rock, paper, or scissors, and determine the winner against a random computer choice.
import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Get user input
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Validate input
if user_choice not in choices:
    print("Invalid choice! Please enter rock, paper, or scissors.")
else:
    # Random choice for the computer
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
    else:
        print("You lose! 😢")
