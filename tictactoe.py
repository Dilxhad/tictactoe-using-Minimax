"""
Tic Tac Toe Player
"""

import math
import copy

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
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1

    if count == 0:
        return
    elif count % 2 == 1:
        return X
    elif count % 2 == 0:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    if board[i][j] != EMPTY:
        raise Exception

    elif 0 <= i <= 2 and 0 <= j <= 2:
        res_board = copy.deepcopy(board)
        res_board[i][j] = player(board)
        return res_board
    raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[1][1]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]

    return


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif not any(EMPTY in row for row in board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        best_score = -9999
        best_action = None
        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    elif player(board) == O:
        best_score = 9999
        best_action = None
        for action in actions(board):
            score = max_value(result(board, action))
            if score <= best_score:
                best_score = score
                best_action = action
        return best_action

    return None


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -9999
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 9999
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
