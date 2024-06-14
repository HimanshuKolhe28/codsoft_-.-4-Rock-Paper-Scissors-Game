# codsoft_-.-4-Rock-Paper-Scissors-Game
summary
ChatGPT
This code implements a simple Rock, Paper, Scissors game where a player competes against the computer. Here's a summary of the code:

Define Options:

A tuple options is created containing the possible choices: "rock", "paper", "scissors".
Game Loop:

An infinite while loop is used to keep the game running until the player decides to stop.
Player Input:

Inside the loop, another while loop ensures that the player inputs a valid choice. The player's input is converted to lowercase to match the options.
Computer Choice:

The computer randomly selects one of the options using random.choice(options).
Display Choices:

Both the player's and the computer's choices are printed.
Determine Winner:

If the player's choice matches the computer's, it's a tie.
The player wins if:
"rock" beats "scissors"
"paper" beats "rock"
"scissors" beats "paper"
Otherwise, the computer wins.
Prompt to Play Again:

The player is asked if they want to play again.
If the player inputs "no", the game loop breaks and exits. If the player inputs anything else, the game continues.
A message thanking the player is printed before the game exits.
