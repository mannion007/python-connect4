from random import randint

player_char = '@'
computer_char = '#'
empty_char = 'O'

board_width = 12
board_height = 10

player_turn = True
game_over = False

board = []

def setup_game():
	for row in range(board_height):
		board.append([empty_char] * board_width)

def render():
	for row in range(len(board)):
		print board[row]

def col_full(col):
	return board[0][col] != empty_char

def board_full():
	for col in range(board_width):
		if not col_full(col):
			return False
	return True

def player_move():
	valid = False
	message = 'Player, choose a column...'

	while not valid:
		col = raw_input(message)
		valid = move_valid(col)
		message = 'Player, that choice is not valid. Please choose another column...'

	move(int(col), player_char)

def computer_move():
	valid = False

	while not valid:
		col = randint(0, board_width - 1)
		valid = move_valid(col)

	print('Computer chose column %s' % str(col))
	move(col, computer_char)

def move(col, char):
	if not col_full(col):
		for row in range(len(board)-1, -1, -1):
			if board[row][col] == empty_char:
				board[row][col] = char
				player_turn = False
				break

def move_valid(col):
	try:
		col = int(col)
	except 	ValueError:
		return False

	if col < 0 or col > board_width - 1:
		return False
	elif col_full(col):
		return False
	return True

def game_won(char):
	for col in range(board_width):
		for row in range(board_height):
			if board[row][col] == char:
				# Horizontal line
				if col + 4 <= board_width:
					if board[row][col + 1] == char and board[row][col + 2] == char and board[row][col + 3] == char:
						return True
				# Vertical line
				if row + 4 <= board_height:
					if board[row + 1][col] == char and board[row + 2][col] == char and board[row + 3][col] == char:
						return True
				# Diagonal down
				if col + 4 <= board_width and row + 4 <= board_height:
					if board[row + 1][col + 1] == char and board[row + 2][col + 2] == char and board[row + 3][col + 3] == char:
						return True
				# Diagonal up
				if col - 4 >= 0 and row - 4 >= 0:
					if board[row - 1][col - 1] == char and board[row - 2][col - 2] == char and board[row - 3][col - 3] == char:
						return True
	return False

def game_over():
	if board_full():
		return True

setup_game()

while not game_won(player_char) and not game_over():
	if player_turn:
		player_move()
		player_turn = False
	else:
		computer_move()
		player_turn = True

	render()

print 'Game over'