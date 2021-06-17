# Rock Paper Scissors
# Justin D
# 10/27/2020
# Filename: Rock Paper Scissors.py


from random import randint

print("Type: Rock, Paper, or Scissor")
player = input()
computer = randint(0,2)


if computer == 0:
	computer = "Rock"
if computer == 1:
	computer = "Paper"
if computer == 2:
	computer = "Scissors"

print("--------")
print("Your choice: " + player)
print("Computer's choice: " + computer)
print("--------")

if player == computer:
	print("Draw")
else:
	if player == "Rock":
		if computer == "Paper":
			print("Lose")
		else:
			print("Win")

	elif player == "Paper":
		if computer == "Scissors":
			print("Lose")
		else:
			print("Win")

	elif player == "Scissors":
		if computer == "Rock":
			print("Lose")
		else:
			print("Win")

	else:
		print("Invalid Input!!!")
		print("Type: Rock, Paper, or Scissor")










