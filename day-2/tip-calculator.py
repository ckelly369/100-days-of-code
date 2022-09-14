print("Welcome to the tip calculator!")
total_before_tip = float(input("What was the total bill? £"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
no_of_people = int(input("How many people will split the bill? "))

tip_amount = total_before_tip * tip_percentage / 100
tip_per_person = tip_amount / no_of_people

# the below code will round the number 2 decimal places, but if the result of the calculation ends in 0, then only one 0 will be displayed e.g. £120.0
# this is a formatting problem in python
# total_per_person = round(total_before_tip / no_of_people + tip_per_person, 2)

# the format function, prefixed with colon, dot and 2, will allow us to show 2 decimal places on the value
total_per_person = "{:.2f}".format(total_before_tip / no_of_people + tip_per_person)

print(f"Each person should pay: £{total_per_person}")