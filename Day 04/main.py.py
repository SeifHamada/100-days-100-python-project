import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = input("Choose Rock Paper or scissors: ").strip().lower()
computer = random.choice(["rock", "paper", "scissors"])

if user == "rock" and computer == "rock":
    print(f"User choice: {rock}")
    print(f"Computer choice: {rock}")
    print("Draw!")

elif user == "rock" and computer == "paper":
    print(f"User choice: {rock}")
    print(f"Computer choice: {paper}")
    print("You lose!")

elif user == "rock" and computer == "scissors":
    print(f"User choice: {rock}")
    print(f"Computer choice: {scissors}")
    print("You win!")

elif user == "paper" and computer == "paper":
    print(f"User choice: {paper}")
    print(f"Computer choice: {paper}")
    print("Draw!")

elif user == "paper" and computer == "rock":
    print(f"User choice: {paper}")
    print(f"Computer choice: {rock}")
    print("You win!")

elif user == "paper" and computer == "scissors":
    print(f"User choice: {paper}")
    print(f"Computer choice: {scissors}")
    print("You lose!")

elif user == "scissors" and computer == "scissors":
    print(f"User choice: {scissors}")
    print(f"Computer choice: {scissors}")
    print("Draw!")

elif user == "scissors" and computer == "rock":
    print(f"User choice: {scissors}")
    print(f"Computer choice: {rock}")
    print("You lose!")

elif user == "scissors" and computer == "paper":
    print(f"User choice: {scissors}")
    print(f"Computer choice: {paper}")
    print("You win!")

else:
    print("Please choose a valid option")






