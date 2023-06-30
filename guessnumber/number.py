import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the correct number.")

    secret_number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        print("\nAttempts remaining:", attempts)
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print("Congratulations! You guessed the number correctly!")
            return

        attempts -= 1

    print("\nGame over! You ran out of attempts.")
    print("The secret number was:", secret_number)

guess_the_number()
