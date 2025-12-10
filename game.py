# Number Guessing Game

import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to Number Guessing Game 🎯")
    print("Guess a number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("⬆ Too Low! Try again.")
        elif guess > secret_number:
            print("⬇ Too High! Try again.")
        else:
            print(f"✅ Correct! You guessed it in {attempts} attempts.")
            break

number_guessing_game()
