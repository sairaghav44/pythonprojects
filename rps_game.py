import random 

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ").lower()

print(f"player : {player}")
print(f"computer : {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "paper":
        print("You lose!")
    else:
        print("You win!")
elif player == "paper":
    if computer == "scissors":
        print("You lose!")
    else:
        print("You win!")
elif player == "scissors":
    if computer == "rock":
        print("You lose!")
    else:
        print("You win!")