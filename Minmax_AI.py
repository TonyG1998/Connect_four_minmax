from anytree import Node, RenderTree
import random
import sys
udo = Node(4)
marc = Node("Marc", parent=udo)
lian = Node("Lian", parent=marc)
dan = Node("Dan", parent=udo)
jet = Node("Jet", parent=dan)


#Converts board so it is easier to navigate when evaluating board positions
def board_convert(board):
	new_board = {}

	x_start = 143
	y_start = 280

	for i in range(1, 7):
		

		for j  in range(1, 8):
			new_board[j, i] = board[x_start, y_start]
			x_start += 36
		x_start = 143
		y_start -= 33

	return new_board
#addes game piece to column
def add_game_piece(board, column, color):
	for i in range(0, 7):
		if board[column, i] == 'None':
			board[column, i] == color
			return True

		return False


def random_pos():
	randx = random.randint(143, 359)
	randy = random.randint(115, 280)

	return (randx, randy)
#Recurvise MinMax algorithm
def MinMax(node, depth, maximizingPlayer):
	if depth == 0 or (node.children == ()):
		return heuristic(node)

	if maximizingPlayer:
		value = -sys.maxsize - 1
		for child in node.children:
			value = max(value, MinMax(child, depth - 1, False))
		return value
	else:
		value = sys.maxsize
		for child in node.children:
			value = min(value, MinMax(child, depth - 1, True))
		return value
#Evaluates the current board state
def heuristic(node, red_turn):
	current_piece
	if red_turn:
		current_piece = 'Red'
	else:
		current_piece = 'Black'
#generate decision tree, work in progress
def generate_game_tree(current_board, red_turn, depth):
	

	if red_turn:
		current_piece = 'Red'
	else:
		current_piece = 'Black'
	
	root = Node(current_board)
	for i in range(1, 8):



	for i in range(0, depth):
		temp_board = current_board
		current_root = root
		for child in current_root:
			for j in range(1, 8):



	

	return root








root = Node(5)
child1 = Node(2, parent=root)
child2 = Node(-5, parent=root)
child11 = Node(7, parent=child1)
child12 = Node(1, parent=child1)
child21 = Node(-4, parent=child2)
child22 = Node(5, parent=child2)

best_num = MinMax(root, 2, True)

root = generate_game_tree()
print(root.children[0].name)
	
