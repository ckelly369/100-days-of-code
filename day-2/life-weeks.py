age = input("Enter your current age: ")

# converting age from str to int
new_age = int(age)

death_age = 90
years_remaining = death_age - new_age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * (52)
months_remaining = years_remaining * (12)

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")