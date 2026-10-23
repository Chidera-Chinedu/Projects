
import random

print("Welcome to the Number Guessing Game!")

while True:
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print("\nI'm thinking of a number between 1 and 20.")
    print("You have only 5 guesses. Don't disappoint me! 😂")

    while attempts < max_attempts:
        try:
            guess = int(input("\nGuess a number from 1 to 20: "))

            if guess < 1 or guess > 20:
                print("That number is outside the range! Try again.")
                continue

            attempts += 1

            if guess > secret_number:
                print("Lower!")
            elif guess < secret_number:
                print("Higher!")
            else:
                print("Winner! 🎉 You actually got it!")
                print(f"You won in {attempts} guesses!")
                break

            remaining = max_attempts - attempts
            print(f"Guesses remaining: {remaining}")

        except ValueError:
            print("Invalid input! Enter a whole number, please.")

    if attempts == max_attempts and guess != secret_number:
        print("\nYOU LOSE! 😂")
        print(f"The secret number was {secret_number}.")
        print("Five guesses and you still couldn't get it? 😭")

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("Thanks for playing! Goodbye! 👋")
        break

