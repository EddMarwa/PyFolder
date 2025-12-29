import random

number = random.randint(1, 100)
guess = None
attempts = 0

while guess != number:
    try:
        guess = int(input("Guess any number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You've guessed the number in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid number.")

