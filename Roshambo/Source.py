import random

player = input("Enter 1 for Rock, 2 for Paper, or 3 for Scissor: ")

player = int(player)

while player < 1 or player > 3:
    print("Invalid input. Try again")
    player = input("Enter 1 for Rock, 2 for Paper, or 3 for Scissor: ")

    player = int(player)

if(player == 1):
    print("You Chose Rock.")
elif(player == 2):
    print("You chose Paper")
elif(player == 3):
    print("You chose Scissor")

computerChoice = random.randint(1, 3)

print(computerChoice)