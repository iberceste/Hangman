from hangman_art import logo
from replit import clear
print(logo)
from hangman_words import word_list
import random

chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for n in range(len(chosen_word)):
    display.append("_")
print(display)
lives = 6
guess_list = []
game_start = True
while game_start:

    guess = input("Guess a letter:").lower()
    clear()
    for letter in range(0, len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess
    if guess not in chosen_word and guess in guess_list:
        lives = lives
    elif guess not in chosen_word:
        lives -= 1
        print(f"Kelimede olmayan {guess} harfini tahmin ettin ")
    for char in guess:
        if guess in guess_list:
            print(f"Zaten {guess} harfını daha once tahmın ettın.")
        guess_list += guess
    print(display)
    from hangman_art import stages

    print(stages[lives])
    if "_" not in display:
        game_start = False
        print("YOU WİN")
    if lives == 0:
        game_start = False
        print("YOU LOSE")