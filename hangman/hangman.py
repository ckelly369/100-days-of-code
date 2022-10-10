import random

# Three words in a list.
# A random word is defined in a new variable.
# Printed the chosen word.
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The word that was chosen is {chosen_word}.")

# Empty list.
# Adding "_" to empty list (number of char from the chosen word).
display = []
word_length = len(chosen_word)

for blank in chosen_word:
    display += "_"

print(display)

# User input.
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

print(display)