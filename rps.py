import random

moves = ["r", "p", "s"]

playerWins = 0
computerWins = 0

print("Welcome to rock, paper, scissors! Best of 3 wins.")

while (playerWins < 3) and (computerWins < 3):

    playerMove = input("What is your move? ")[0].lower()
    if not (playerMove == "r" or playerMove == "p" or playerMove == "s"):
        print("Please enter a valid move!")
        continue

    computerMove = moves[random.randrange(0, 3)]

    computerPlayed = "The computer played "
    if computerMove == "r":
        print(computerPlayed + "rock!")
    elif computerMove == "p":
        print(computerPlayed + "paper!")
    else:
        print(computerPlayed + "scissors!")

    if computerMove == playerMove:
        print("It's a tie!")
    elif (playerMove == "r" and computerMove == "s") or (playerMove == "s" and computerMove == "p") or (playerMove == "p" and computerMove == "r"):
        print("Player wins!")
        playerWins += 1
    else:
        print("Computer wins!")
        computerWins += 1
        
if playerWins > computerWins:
    print("Game over! The player wins, " + str(playerWins) + " to " + str(computerWins) + ".")
else:
    print("Game over! The computer wins, " + str(computerWins) + " to " + str(playerWins) + ".")