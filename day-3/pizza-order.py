print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L. ").upper()
pepperoni = input("Do you want pepperoni? Y or N. ").upper()
extra_cheese = input("Do you want extra cheese? Y or N. ").upper()

bill = 0

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"The final bill is £{bill}.")