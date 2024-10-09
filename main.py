# Aditya Kunapareddy
# Create a number guessing game

import random


def play_game():
    # Randomly choose a number between 1 and 100
    secret_number = random.randint(1, 100)
    guesses = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Type 'quit' at any time to exit the game.")

    while True:
        guess = input("Enter your guess: ").lower()

        if guess == 'quit':
            print("Thanks for playing! The number was", secret_number)
            return

        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number or 'quit'.")
            continue

        guesses += 1

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low. Please guess higher.")
        elif guess > secret_number:
            print("Too high. Please guess lower.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {guesses} {'guess' if guesses == 1 else 'guesses'}.")
            return


if __name__ == "__main__":
    play_game()