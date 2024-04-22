import random, os
from hangman_stages import stages
from hangman_wordlist import word_list

clear = lambda: os.system('clear')

chosen_word = random.choice(word_list).lower()
display = ["_"] * len(chosen_word)

end_of_game = False
lives = 6

while not end_of_game:
    clear()
    print(" ".join(display).upper())
    print(stages[6-lives] + "\n")
    guess = str(input("Rate einen Buchstaben: ")).lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                display[index] = guess
    else:
        lives -= 1

    if "_" not in display or lives == 0:
        end_of_game = True
        
clear()
print(" ".join(list(chosen_word)).upper())
print(stages[6-lives] + "\n")
if lives > 0:
    print("Du hast gewonnen.")
else:
    print("Du hast verloren.")