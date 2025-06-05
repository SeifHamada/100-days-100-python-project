from art import logo, vs
import random
from game_data import data

def get_random_account():
    return random.choice(data)

def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(choice, a_followers, b_followers):
    if choice == 'a':
        return a_followers > b_followers
    elif choice == 'b':
        return b_followers > a_followers
    else:
        return False

def play_game():
    score = 0
    a = get_random_account()
    b = get_random_account()

    while True:
        print(logo)
        print(f"Compare A: {format_account(a)}")
        print(vs)
        print(f"Against B: {format_account(b)}")

        choice = input("Who has more followers? Type 'a' or 'b': ").lower().strip()

        a_followers = a["follower_count"]
        b_followers = b["follower_count"]

        is_correct = check_answer(choice, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}\n")
            a = b
            b = get_random_account()
            while a == b:
                b = get_random_account()
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

play_game()
