import random
from art import logo
print(logo)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()

def easy():
    easy_attempts = 10
    answer = random.randint(1, 100)
    print("You have 10 attempts remaining to guess the number.")
    while easy_attempts > 0:
        easy_guess = int(input("Make a guess: "))
        easy_attempts -= 1
        if easy_guess < answer:
            print("Too low.")
            print("Guess again.")
            print(f"You have {easy_attempts} attempts remaining to guess the number.")


        elif easy_guess > answer:
                print("Too high.")
                print("Guess again.")
                print(f"You have {easy_attempts} attempts remaining to guess the number.")


        elif easy_guess == answer:
            print(f"You got it! the answer was {answer}.")
            break

        else:
            print(f"You've run out of guesses. Refresh the page to try again. the answer was{answer}.")
            break

def hard():
    attempts = 5
    answer = random.randint(1, 100)
    print("You have 5 attempts remaining to guess the number.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess < answer:
            print("Too low.")
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")

        elif guess > answer:
            print("Too high.")
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")

        elif guess == answer:
            print(f"You got it! the answer was {answer}.")
            break

        else:
            print(f"You've run out of guesses. Refresh the page to try again. the answer was{answer}.")


if difficulty == 'easy':
    easy()

elif difficulty == 'hard':
    hard()

else:
    print("Please choose either 'Easy' or 'Hard'")