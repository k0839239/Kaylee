"""
We want to make an unbeatable Tic-Tac-Toe game, with an AI that will never lose.
For that to happen, we will be making use of Functions/Methods, Lists, and If/Else statements.
Go through this code and follow the instructions carefully.
"""

"""
Part 1: Making the board
To start our game off, we need a board!
I want you to make a function called 'make_board()' that takes no arguments/parameters.
This board should return a 3x3 matrix aka list of lists. The list of lists should be no more than
two levels deep. For example, I should be able to only have to call board[1][1] to get the the middle
position on the board.
Each "cell" should have a default value of an underscore, '_'.

If you need help consult the notes from Week4.py.
"""


"""
Part 2: Printing the Game Board
Now we need to show the user the game board.
To do this, I want you to figure out how to print out the board each time.
To get you started, you should make a function called 'print_board(board)'.
Note that this function takes in a board as its parameter.

Bonus EC: Figure out how to clear the playing field before the board is printed.
Hint, it may be wise to 'import sys', but what from sys can we use???
"""

    
"""
Part 3: Making the move for the player
The game doesn't really work unless the player actually plays the game.
What I want you to do is to make a function called 'make_move(board)' that takes in board.
This function should get the 'input' from the user. Make sure there is some meaningful text,
such as: "Enter the x,y pair for an available position:"
You should take this input and 'split' it on a comma ','.
Then you should make the move of the PLAYER onto the board, by calling the correct position
on the board. Just set it to the value PLAYER, which is 'X'.
Bonus EC: Figure out a way checking whether or not the user made a valid choice.
"""


"""
Part 4: Checking the winning state
Finally, we need to be able to determine whether or not someone actually won.
Write a function 'winning(current_player, board)' that takes two parameters, current_player and board.
Using if/elif/else statments check whether or not that player has won the game and 'return' a value of True if so.
'Else, return False'
Note that there are a total of 8 potential ways of winning the game of Tic-Tac-Toe.
"""



##############################################################
# Test Code
##############################################################
PLAYER = 'X'
AI = 'O'

def print_help():
    print("""
This is a game of Tic-Tac-Toe, where you, the player, will compete
against a small Artificial Intelligence (AI) based on the Minimax 
Algorithm in Game Theory.

The Rules of Tic-Tac-Toe are simple. There are a total of 9 positions
on the board, shown below. The player is represented by 'X' and the AI
by 'O'. Get 3 X's in a row and you win!

The board is represented like so:

         1 | 2 | 3
        -----------
         4 | 5 | 6
        -----------
         7 | 8 | 9 
    """)

def evaluate(board):
    """
    Heuristic function to evaluate the current state of the game
    :param board: Current board layout
    :return: +1 if computer wins, -1 if the player wins, 0 for draw
    """
    if winning(AI, board):
        return 1
    elif winning(PLAYER, board):
        return -1
    return 0
    
def available_moves(board):
    """
    Gets a list of available moves left
    :param board: Current board
    :return: List of available moves
    """
    cells = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if col == '_':
                cells.append([x, y])
    return cells

def won_state(board):
    """
    Returns whether or not the game is in a won state.
    :param board: The current board
    :return: True if the game is won
    """
    return winning(PLAYER, board) or winning(AI, board)

def swap_player(player):
    """
    Swaps the current player
    :param player: Current player
    :return: Either PLAYER or AI
    """
    if player == AI:
        return PLAYER

    return AI

def minimax(board, depth, player):
    """
    Minimax Algorithm used in Game Theory for finding optimal move for a player
    :param board: Current board
    :param depth: Node index in the tree; 0 <= depth < 9
    :param player: Human player or computer
    :return: List with best move and score
    """

    """
    See if you can figure out the Minimax Algorithm. The pseudocode reads as follows:

    if board is a terminal state:
        return value of the board
    
    for each move in available moves:
        set the board to the current player
        calculate the minimax
        set board back to original state

        if player is AI:
            return the max of best score and score
        else:
            return the min of best score and score
    
    return best as the x,y of the move and the score
    """
    pass

if __name__ == "__main__":
    from math import inf as infinity
    import itertools
    # print_help()
    
    current_player = PLAYER
    board = make_board()
    
    while len(available_moves(board)):
        print_board(board)
        
        if current_player == PLAYER:
            make_move(board)
        else:
            depth = len(available_moves(board))
            best_move = minimax(board, depth, AI)
            board[best_move[0]][best_move[1]] = AI
        
        # Check for winner
        if winning(current_player, board):
            print_board(board)
            print(f'Congratulations Player {current_player}')
            print('You win!')
            break
        elif not len(available_moves(board)):
            print('Draw!')
        
        current_player = swap_player(current_player)