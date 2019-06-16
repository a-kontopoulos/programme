
def guessingGame(secret_colour, secret_number):
    number = input("Please a number between 1 and 20: ")
    colour = input("Please could you give me now a colour: ")
    if secret_colour == colour and secret_number == int(number):
        print("You've found both the secret number and the secret color!")
    elif secret_colour == colour or secret_number == int(number):
        print("You found at least one of the secrets!")
    else:
        print("You didn't find any of the secrets! and Better luck next time!")

guessingGame("red", 4)