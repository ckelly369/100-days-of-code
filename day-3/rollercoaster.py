print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You are tall enough to ride.")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("It will cost you £5.")
    elif age <=18:
        bill = 7
        print("It will cost you £7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("It will cost you £0.")
    else:
        bill = 10
        print("It will cost you £10.")
    
    photo = input("Do you want to add a photo for £5? Y or N. ").upper()
    if photo == "Y":
        bill += 5
    print(f"The total bill is £{bill}.")

else:
    print("Sorry, you are not tall enough to ride.")