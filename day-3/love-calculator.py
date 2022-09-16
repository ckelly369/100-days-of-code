print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

# the values are wrapped in str() because this will concatenate the actual values, and not add them mathematically
love_score = str(true) + str(love)
# this converts the str to int. Alernatively, we could wrap the above in int() at the beginning of str(true)
int_score = int(love_score)

if int_score < 10 or int_score > 90:
    print(f"Your score is {int_score}, you go together like coke and mentos.")
elif int_score >= 40 and int_score <= 50:
    print(f"Your score is {int_score}, you are alright together.")
else:
    print(f"Your score is {int_score}.")
