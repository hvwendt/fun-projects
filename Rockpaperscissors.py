import random 
user = input("Enter a choice (rock, paper, scissors): ")
possibleActions = ["rock", "paper", "scissors"]
computerAction = random.choice(possibleActions)
print("You chose " + user + " computer chose " + computerAction)


if user == computerAction:
	print("It's a tie")
elif user == "rock":
	if computerAction == "scissors":
		print("Rock smashes scissors. You win!")
	else:
		print("Paper covers rock! You lose. ")
elif user =="paper":
	if computerAction =="rock":	
		print("Paper covers rock! You win!")
	else:
		print("+Scissors cuts paper! You lose.")
elif user == "scissors":
	if computerAction == "paper":
		print("Scissors cuts paper! You win!")
	else: 
		print("Rock smashes scissors. You lose")


