player_char = '@'
computer_char = '#'
empty_char = 'O'

board_width = 12
board_height = 10

game_over = False
board = []

def setup_game():
	game_over = False
	
	for row in range(board_height):
		board.append([empty_char] * 12)

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

def move(col, char):
	if not col_full(col):
		for row in range(len(board)-1, -1, -1):
			if board[row][col] == empty_char:
				board[row][col] = char
				break

while True:
	setup_game()
	while not game_over:
		move(int(raw_input('Player, choose a column...')), player_char)
		render()