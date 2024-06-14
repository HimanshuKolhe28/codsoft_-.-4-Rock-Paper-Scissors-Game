'''
Problem Statement 
User Input: Prompt the user to choose rock, paper, or scissors.

Computer Selection: Generate a random choice (rock, paper, or scissors) for

the computer.

Game Logic: Determine the winner based on the user's choice and the

computer's choice.

Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice.

Display the result, whether the user wins, loses, or it's a tie.

Score Tracking (Optional): Keep track of the user's and computer's scores for

multiple rounds.

Play Again: Ask the user if they want to play another round.

User Interface: Design a user-friendly interface with clear instructions and

feedback.
'''


import random

options = ("rock", "paper", "scissors")

while True:
    player = None
    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    computer = random.choice(options)
     
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("Player wins!")
    else:
        print("Computer wins!")

    Next_game = input("Let's play again? (yes/no): ")
    if Next_game.lower() == "no":
      #  break
    #else:
        print ("Thank for playing with us..")
