# Python-game
The game is played on a 3x3 grid. Each player takes turns placing their symbol (either "X" or "O") in an empty square on the grid. 
The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins the game. 
If all squares are filled without a winner, the game is a tie.

Here's a brief overview of the code:

The print_board() function takes a list representing the current state of the board and prints it to the console in a nicely formatted way.

The get_move() function prompts the current player to enter their move (a number between 1 and 9 corresponding to a square on the grid), 
validates the input, and returns the move as an integer index into the board list.

The check_win() function checks the current state of the board for any winning combinations of X's or O's 
(using a list of all possible winning combinations), and returns True if a winning combination is found, and False otherwise.

The tic_tac_toe() function initializes the board to be empty, then loops through turns alternating between X and O players. 

It prints the board at the beginning of each turn, prompts the current player to enter their move, and updates the board if the move is valid. 

It continues looping until either a player wins or the board is full. Finally, it prints the final state of the board and declares the winner or a tie.
