# ----------------------------- v5.0 code --------------------------------
from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("..........Rock..........")
    print("..........Paper..........")
    print("..........Scissors..........")

    player = input("Make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer == "scissors"
    print(f"Computer plays {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    else:
        print("Please enter a valid move!")
if player_wins > computer_wins:
    print("CONGRATS! YOU BEAT THE COMPUTER!")
else:
    print("Oh no:( THANKS FOR TRYING!")
print(
    f"FINAL SCORES... YOU: {player_wins} COMPUTER : {computer_wins}")
