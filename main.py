import random


def guess_the_number(x):
    random_number = random.randint(1,x)
    guess = None

    while guess != random_number:
        guess=int(input(f"\n Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
    print(f"Congrats! You guessed the correct number {random_number}")
    

# guess_the_number(5)


def computer_guessing_the_number(x):
    low = 1
    high = x
    feedback = ""
    number=input(f"Consider a number from {low} to {high}, Which computer will guess :")
    print(f"The number you have assumed is {number}\n")
    while feedback != "C" :
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = high #or guess = low , both are same
    
        feedback = input(f" {guess} is Computer Guess, Its too low (l) or Its too high (h) or Its correct (c) :").upper()

        if feedback == "L":
            low = guess + 1
        elif feedback == "H":
            high = guess - 1

    print("Yea! The computer Guessed the correct number that you assumed",number)

# computer_guessing_the_number(50)
print("🎮 Welcome to the Number Guessing Game!")
print("Choose your mode:")

while True:
        user_input = int(input("1️⃣  You guess the computer's number or 2️⃣  The computer guesses your number :"))
        try:
            if user_input == 1:
                guess_the_number(100)
                break 
            elif user_input == 2:
                computer_guessing_the_number(100)
                break 
            else:
                print("Invalid input,Try again!!!")

        except ValueError :
            int("That’s not a number. Try again with 1 or 2.")