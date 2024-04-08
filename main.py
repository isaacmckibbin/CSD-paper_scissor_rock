import random

options = ("rock", "paper", "scissor")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock, paper, scissor): ")

print(f"Player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "scissors" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("You win!")

import random

options = ("rock", "paper", "scissor")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock, paper, scissor): ")

print(f"Player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "scissors" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("You Win!")


import random

options = ("rock", "paper", "scissor")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter a choice (rock, paper, scissor): ")

print(f"Player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "scissors" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("You lose!")


print("thank for playing!")
print("play again soon!(:")
print("by Isaac") 
