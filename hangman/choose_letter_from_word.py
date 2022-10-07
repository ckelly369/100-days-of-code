import random
from subprocess import check_output

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ")

for letter in chosen_word:
    if letter == guess:
        print(f"Correct - the word is {chosen_word}")
    else:
        print(f"Incorrect - the word is {chosen_word}")