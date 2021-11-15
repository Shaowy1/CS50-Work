"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

rows = 3
cols = 3


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    piece_count = 0
    if terminal(board) == True:
        return None
    else:
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X" or board[row][col] == "O":
                    piece_count += 1

        if board == initial_state():
            return "X"

        if piece_count % 2 == 0:
            return "X"
        else:
            return "O"


def actions(board):
    if terminal(board):
        return None
    else:
        actions_set = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == None:
                    actions_set.add((row, col))

        return actions_set



def result(board, action):
    current_player = player(board)
    new_board = copy.deepcopy(board)
    if current_player == "X":
        new_board[action[0]][action[1]] = "X"
    else:
        new_board[action[0]][action[1]] = "O"

    return new_board


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
            else:
                return None
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
        else:
            return None
    return None

def fullBoard(board):
    board_filled = True
    for row in range(rows):
        for col in range(cols):
            if (board[row][col]) == EMPTY:
                board_filled = False

    return board_filled

def terminal(board):
    if winner(board) != None:
        return True
    elif fullBoard(board):
        return True
    else:
        return False


def utility(board):
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    current_player = player(board)

    if terminal(board):
        return None

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            temp = min_value(result(board, action))
            if temp > v:
                v = temp
                optimal = action
    else:
        v = math.inf
        for action in actions(board):
            temp = max_value(result(board, action))
            if temp < v:
                v = temp
                optimal = action

    return optimal
            

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        temp = min_value(result(board, action))
        v = max(v, temp)
        
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        temp = max_value(result(board, action))
        v = min(v, temp)

    return v