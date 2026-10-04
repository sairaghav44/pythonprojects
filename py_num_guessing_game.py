import random 

Lowest_number = 1
highest_number = 100
answer = random.randint(Lowest_number, highest_number)
guesses  = 0
is_running = True

print ("lets  play a number guessing game :) ")
print(f"Please select a number between {Lowest_number} and {highest_number}")

while is_running:

    guess = input("enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < Lowest_number or guess > highest_number:
            print("the entered number is out of range")
            print(f"Please select a number between {Lowest_number} and {highest_number}")

        elif guess < answer:
            print("your guess is too low, try again")
        elif guess > answer:
            print("your guess is too high, try again")
        else:
            print(f"Congratulations! You guessed the number in {guesses} tries.")
            print(f"the answer was {answer}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please select a number between {Lowest_number} and {highest_number}")
