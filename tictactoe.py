"""
Tic Tac Toe Player
For all functions that accept a board as input, you may assume that it is a valid
board (namely, that it is a list that contains three rows, each with three values of
either X, O, or EMPTY). You should not modify the function declarations (the order
or number of arguments to each function) provided.
Once all functions are implemented correctly, you should be able to run python
runner.py and play against your AI. And, since Tic-Tac-Toe is a tie given optimal play
by both sides, you should never be able to beat the AI (though if you do not play
optimally as well, it may beat you!)
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    else:
        count = 0
        for i in 3:
            for j in 3:
                if board[i][j] is EMPTY:
                    count+=1
    if count % 2 is 1:
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    mySet = set()
    for i in 3:
            for j in 3:
                if board[i][j] is not EMPTY:
                    mySet.add((i,j))
    return mySet

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    currPlayer = player(board)
    boardCopy = deepcopy(board)
    if action < (3,3) and action >= (0,0) and board[action[0]][action[1]] == EMPTY:
        boardCopy[action[0]][action[1]] = currPlayer
    else:
        raise Exception("Invalid Move")
    return boardCopy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]
    for x in 2:
        if board[x][0] == board[x][1] == board[x][2] and board[x][0] != EMPTY:
            return board[x][0]
        if board[0][x] == board[1][x] == board[2][x] and board[0][x] != EMPTY:
            return board[x][0]
    return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (sum(row.count(EMPTY) for row in board) == 0) or winner(board) != None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
     The minimax function should take a board as input and return the optimal
move for the player to move on that board.
❖ The move returned should be the optimal action (i, j) that is one of the
allowable actions on the board. If multiple moves are equally optimal,
any of those moves is acceptable.
❖ If the board is a terminal board, the minimax function should return
None.

    """
    raise NotImplementedError
