import random

print("Welcome to the rock, paper and scissor game.")
user_choice = int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissor :- "))

resMatrix = [
    ["Draw", "Lose", "Won"],
    ["Won", "Draw", "Lose"],
    ["Lose", "Won", "Draw"],
]

randNum = random.randint(0, 2)
if (user_choice > 2 or user_choice < 0):
    print("Invailid input")
else:
    computer_choice = "Rock" if randNum == 0 else "Paper" if randNum == 1 else "Scissor"

    print(f"Computer selected {computer_choice}. So the result for you :- {resMatrix[user_choice][randNum]}")