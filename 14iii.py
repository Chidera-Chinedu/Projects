import random

secret_number = random.randint(1, 20)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 20. Can you guess it?")

while True:
    try:
        guess = int(input("Guess a number from 1 to 20: "))
        attempts += 1

        if guess < 1 or guess > 20:
            print("Please choose a number between 1 and 20!")

        elif guess > secret_number:
            print("Lower")

        elif guess < secret_number:
            print("Higher")

        else:
            print("Winner!")
            break

    except ValueError:
        print("Error: Please enter a  whole numerical value!")