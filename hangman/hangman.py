import random
import hangman_art
from word_list import words

# Three words in a list.
# A random word is defined in a new variable.
# Printed the chosen word.
print(hangman_art.logo)
word_list = words
chosen_word = random.choice(word_list)
print(f"The word that was chosen is {chosen_word}.")

# Empty list.
# Adding "_" to empty list (number of char from the chosen word).
display = []
word_length = len(chosen_word)

for blank in chosen_word:
    display += "_"

print(display)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # The range is between 0 and the word length (length of chosen word).
    # On the first run, the position of chosen_word is index 0.
    # So the letter variable becomes equal to the first letter of the chosen word.
    # Statement to check if the letter matches the guess.
    # If False, go back to the for loop and move to next index position.
    # If True, look at the list (display) and replace the blank with the matching letter.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You now have {lives} lives.")
        if lives == 0:
            end_of_game = True
            print("Game over.")
    print(display) 

    if "_" not in display:
        end_of_game = True
        print("You have won!")

print(hangman_art.stages[lives])