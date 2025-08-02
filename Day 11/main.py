import art
import random

player_cards = []
computer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
target = 21

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
if play == 'y':
    print(art.logo)
    player_cards = random.sample(cards, 2)
    computer_cards = random.choices(cards)
    print(f"Your Cards{player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {computer_cards}")
    while True:
        choose = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
        if choose == 'y':
            player_cards.append(random.choice(cards))
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            computer_cards.append(random.choice(cards))
        else:
            computer_cards.append(random.choice(cards))
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

            if sum(player_cards) > 21:
                print("You went over. You lose.")
            elif sum(computer_cards) > 21:
                print("Computer went over. You Win.")
            elif abs(sum(player_cards) - target) < abs(sum(computer_cards) - target):
                print("You Win!")
            elif abs(sum(player_cards) - target) > abs(sum(computer_cards) - target):
                print("You Lose!")
            else:
                print("Its a tie!")
            break
else:
    print("")
