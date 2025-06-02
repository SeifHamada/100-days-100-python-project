import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print (logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letters in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

correct = []
while True:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower().strip()
    
    if guess in correct:
        print(f"You've already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct.append(letter)
        elif letter in correct:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
            break

    if "_" not in display:
        print("****************************YOU WIN****************************")
        break

    print(stages[lives])