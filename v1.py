from random import randint

player_wins = 0
computer_wins = 0
winning_score = 2

while (player_wins < winning_score) and (computer_wins < winning_score):
	print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
	print("....rock......")
	print("....paper.....")
	print("....scissors..")

	player = input("Enter your choice: ").lower()
	if player == "quit" or player == "q":
		break

	random_num = randint(0,2)

	if (random_num == 0):
		computer = "rock"
	elif (random_num == 1):
		computer = "paper"
	else:
		computer = "scissors"

	print(f"The computer plays: {computer}")

	if player == computer:
		print("It's a tie....")
	elif player == "rock":
		if computer == "paper":
			print("Computer wins...")
			computer_wins += 1
		else:
			print("Player wins...")
			player_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("Player wins...")
			player_wins += 1
		else:
			print("Computer wins...")
			computer_wins += 1
	elif player == "scissors":
		if computer == "rock":
			print("Computer wins")
			computer_wins += 1
		else:
			print("Player wins...")
			player_wins += 1
	else:
		print("Please enter a valid move....")
		
if player_wins > computer_wins:
	print("CONGRATS, YOU WON!!!!!")
elif player_wins == computer_wins:
	print("IT'S A TIE")
else:
	print("OH NO.... THE COMPUTER WON...")
	