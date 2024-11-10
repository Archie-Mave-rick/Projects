import random

print("Dice Roller 2.0")
print("---------------")

print("How many dice would you like to roll?")
# Validate input
while True:
    try:
        numberPicked = int(input("Enter an integer between 1 and 10"))
        if(numberPicked > 0 and numberPicked < 10):
            break
        else:
            print("Invalid input, try again.")
    except:
        print("Please provide an integer")


def rollDice(amountofDice):
    possibleFaces = [1, 2, 3, 4, 5, 6]
    for die in range(amountofDice):
        roll = random.choice(possibleFaces)
        print("Die ", die + 1, ": ", roll)


rollDice(numberPicked)
