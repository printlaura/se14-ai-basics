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

    if terminal(board) == True:
       return "The game is over."

    moves_x = 0
    moves_o = 0
    
    if board == initial_state():
        return X
    else:
        for row in board:
            moves_x += row.count(X)
            moves_o += row.count(O)

    if moves_x > moves_o:
        return O
    elif moves_x <= moves_o:
        return X


def actions(board):

    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board) == True:
        return "The game is over."
    else:
        possible_actions = set()

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == EMPTY:
                    possible_actions.add((i, j))
                else:
                    continue

        return possible_actions


def result(board, action):

    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board_state = copy.deepcopy(board)
    possible_actions = actions(board)

    if action not in possible_actions:
        raise Exception
    elif action in possible_actions:
        i, j = action
        new_board_state[i][j] = player(board)

    return new_board_state


def winner(board):

    """
    Returns the winner of the game, if there is one.
    """

    players = [X, O]

    for player in players:

        for i in board:
           if i == [player, player, player]:
                winner = player
                return winner
            
        for j in range(0,3):
            if [board[i][j] for i in range(0,3)] == [player, player, player]:
                winner = player
                return winner

        if [board[i][i] for i in range(0,3)] == [player, player, player]:
                winner = player
                return winner
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
                winner = player
                return winner
            
    return None


def terminal(board):

    """
    Returns True if game is over, False otherwise.
    """

    if (winner(board) != None) or (EMPTY not in (item for sublist in board for item in sublist)):
        return True
    else:
        return False   


def utility(board):

    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif winner(board) == None:
        return 0


def minimax(board):

    """
    Returns the optimal action for the current player on the board.
    """
    
    #values for alpha-beta pruning
    alpha = -math.inf
    beta = math.inf

    #returns the maximized value of the board state.
    def max_value(board, alpha, beta):

        optimal_move = ()

        if terminal(board):
            return [utility(board), optimal_move]
        else:
            v = -math.inf
            for action in actions(board):
                v = max(v, min_value(result(board, action), alpha, beta)[0])
                optimal_move = action

                if v >= beta:
                    break
                
                if v > alpha:
                    alpha = v

                print(v)#log to debug

        return [v, optimal_move]

    #returns the mainimum value of the board state.
    def min_value(board, alpha, beta):
        
        optimal_move = ()

        if terminal(board):
            return [utility(board), optimal_move]
        else:
            v = math.inf
            for action in actions(board):
                v = min(v, max_value(result(board, action), alpha, beta)[0])
                optimal_move = action

                if v <= alpha:
                    break

                if v < beta:
                    beta = v

                print(v) #log to debug

        return [v, optimal_move]

    if terminal(board):
        return None

    if player(board) == X:
        optimal_action = max_value(board, alpha, beta)[1]
    elif player(board) == O:
        optimal_action = min_value(board, alpha, beta)[1]
    
    return optimal_action

