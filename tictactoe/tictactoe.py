"""
Tic Tac Toe Player
"""

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
	x_count = sum(row.count(X) for row in board)
	o_count = sum(row.count(O) for row in board)
	
	if x_count <= o_count:
		return X
	else:
		return O


def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	actions = set()
	for i, row in enumerate(board):
		for j, cell in enumerate(row):
			if cell == EMPTY:
				actions.add((i, j))
	return actions


def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	if action is None:
		raise Exception("Invalid action: action is None")
	i, j = action
	if board[i][j] != EMPTY:
		raise Exception("Invalid action: cell is not empty")
	if (i < 0 or i > 2) or (j < 0 or j > 2):
		raise Exception("Invalid action: cell is out of bounds")
	new_board = [row.copy() for row in board]
	new_board[i][j] = player(board)
	return new_board


def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
			return board[i][0]
	for j in range(3):
		if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
			return board[0][j]
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
		return board[0][0]
	if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
		return board[0][2]
	return None



def terminal(board):
	"""
	Returns True if game is over, False otherwise.
	"""
	if winner(board) is not None or all(cell is not EMPTY for row in board for cell in row):
		return True
	else:
		return False


def utility(board):
	"""
	Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
	"""
	winning_player = winner(board)
	if winning_player == X:
		return 1
	elif winning_player == O:
		return -1
	else:
		return 0


def max_value(board):
	min = -math.inf
	best_action = None

	if terminal(board):
		return utility(board), None
 
	for action in actions(board):
		v, _ = min_value(result(board, action))
		if v > min:
			min = v
			best_action = action
	return min, best_action

def min_value(board):
	max = math.inf
	best_action = None

	if terminal(board):
		return utility(board), None
 
	for action in actions(board):
		v, _ = max_value(result(board, action))
		if v < max:
			max = v
			best_action = action
	return max, best_action

def minimax(board):
	"""
	Returns the optimal action for the current player on the board.
	"""
	if terminal(board):
		return None

	current_player = player(board)
 
	if (current_player == X):
		_, action = max_value(board)
	elif (current_player == O):
		_, action = min_value(board)
	if (action is None):
		raise Exception("Invalid minimax action: action is None")
	return action