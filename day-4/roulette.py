import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# # Getting the length for names
no_of_people = len(names)

# # Randomising from index 0 to last position in no_of_people
random_choice = random.randint(0, no_of_people -1)

# # Payee will be the random choice in names
payee = names[random_choice]

print(f"{payee} is going to buy the meal today!")

# Alternatively, and in much less code, we could use the random.choice function
# This makes more sense, but was important to understand the above
person_to_pay = random.choice(names)
print(person_to_pay)