from dis import dis
import random
from turtle import pos
import hangman_art
from word_list import words
import os

# Three words in a list.
# A random word is defined in a new variable.
# Printed the chosen word.
print(hangman_art.logo)
end_of_game = False
lives = 6
word_list = words
chosen_word = random.choice(word_list)

print(f"The word that was chosen is {chosen_word}.")

# Empty list.
# Adding "_" to empty list (number of char from the chosen word).
display = []
word_length = len(chosen_word)

for blank in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('clear')

    # The range is between 0 and the word length (length of chosen word).
    # On the first run, the position of chosen_word is index 0.
    # So the letter variable becomes equal to the first letter of the chosen word.
    # Statement to check if the letter matches the guess.
    # If False, go back to the for loop and move to next index position.
    # If True, look at the list (display) and replace the blank with the matching letter.
    if guess in display:
        print(f"You have already selected {guess}, try another letter.")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(hangman_art.stages[lives])
    print(f"\n{' '.join(display)}\n")

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter you selected is not in the word.\nYou now have {lives} lives remaining.")
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("Game over.")

    if "_" not in display:
        end_of_game = True
        print("You have won!")