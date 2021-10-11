"""
Tic Tac Toe Player
"""
# This program consists of methods that are created for a tic tac toe game between a computer and a user

from copy import deepcopy
import math

# Global Variables
X = "X"
O = "O"
EMPTY = None

# Returns an empty board with no moves
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


# Returns the next player's turn
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    if board == initial_state():
        return X
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is X:
                xCount +=1
            if board[i][j] is O:
                oCount +=1
    if xCount > oCount:
        return O
    else:
        return X


# Returns the a set of all actions that are possible
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    mySet = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                mySet.add((i,j))
    return mySet

# Returns the board after the move is made
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    currPlayer = player(board)
    boardCopy = deepcopy(board)
    if board[action[0]][action[1]] == EMPTY:
        boardCopy[action[0]][action[1]] = currPlayer
    else:
        raise Exception("Invalid Move")
    return boardCopy

# Returns the winner of the game
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for x in range(len(board)):
        if board[x][0] == board[x][1] == board[x][2] and board[x][0] != EMPTY:
            return board[x][0]
        if board[0][x] == board[1][x] == board[2][x] and board[0][x] != EMPTY:
            return board[0][x]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None

# Returns a boolean based on the game results
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptyCount =0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:
                emptyCount +=1
    if emptyCount == 0 or winner(board) != None:
        return True
    return False


# Returns 1 if X won the game, -1 if 0 has won, and 0 if its a tie

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else -1 if winner(board) == O else 0

# Returns the best action for the current player on the board
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maxVal(board):
        if terminal(board):
            return utility(board)
        score = -math.inf
        for action in actions(board):
            score = max(score, minVal(result(board, action)))
        return score

    def minVal(board):
        if terminal(board):
            return utility(board)
        score = math.inf
        for action in actions(board):
            score = min(score, maxVal(result(board, action)))
        return score

    if terminal(board):
        return None
    if board == initial_state():
        return (0,0)

    if player(board)== X:
        score = -math.inf
        moveList = []
        for action in actions(board):
            score = max(score, minVal(result(board, action)))
            if score == 1:
                return action
            if score > -1:
                moveList.append((score, action))
        return moveList[0][1]

    else:
        score = math.inf
        moveList = []
        for action in actions(board):
            score = min(score, maxVal(result(board, action)))
            if score == -1:
                return action
            if score < 1:
                moveList.append((score, action))
        return moveList[0][1]
