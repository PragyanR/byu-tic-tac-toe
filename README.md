# BYU Final Project
### Pragyan Ramamoorthy

### Project: Implementation of Tic-Tac-Toe in an Object-Oriented Approach

Tic-Tac-Toe is a two-player game (Wikipedia reference on how the game is played). The game will be played by running a Python file on a Terminal or an IDE. The implementation will ask for each player to enter their name, to begin with, and can continue to play after each game or end. The program will keep track of the number of wins and losses by each player.

**Rules and objectives:**

You may only enter coordinates in range {0-2},{0-2} ex. 1,2
Objectives: Beat your friend by getting three in a row.

The game will first ask for the names of the 2 players. Then the players can enter coordinates (ex.(1,2)) to place their markers on the board. After the game, the computer announces the winner and then asks them if they want to play again.

**Design:** 

Object-Oriented Approach
There will be two classes and a controller. 

**Class 1: Game**
This class contains all the functions required to run Tic-Tac-Toe
Below are the functions in the class:
1.	The “print_board” function displays the board
2.	The “update_board” function gets the coordinates and puts them on the board.
3.	The “check” function checks the board to see if there are any winners


**Class 2: Player**
This class is used to keep track of player information.

**Class 3: Score**
This class contains all functions required to keep track of the score.

Below are the functions in the class:
1.	The “print_score” function displays the score
2.	The “update_score” function updates the score 

**Python Script: Game Controller**
This is the main Python code that creates the objects and orchestrates the game
The main parts of this are:
1.	The new game function runs after every game is done.
2.	A while true loop, that loops the game until they say stop in the new game function.

