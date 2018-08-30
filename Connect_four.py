
import pygame
import os
import Logic
import time


#Function to recieve images and avoid cross-platform errors
_image_library = {}
def get_image(path):
	global _image_library
	image = _image_library.get(path)
	if image == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		image = pygame.image.load(canonicalized_path)
		_image_library[path] = image
	return image

def create_game_board(board):
	x_start = 143
	y_start = 280

	for i in range(0, 7):
		y_start = 280
		for j in range(0, 6):
			board[x_start, y_start] = "None"
			y_start-=33
		x_start+=36
#Places the correct piece in the correct spot after the user clicks on the board
def add_piece(pos, red_turn, board):
	global black
	global red
	x_start = 143
	gap = 14
	x_key = 0
	y_key = 280
	

	for i in range(0, 7):
		if abs(pos[0] - x_start) < gap:
			x_key = x_start
			break
		x_start += 36

	while(board[x_key, y_key] is not 'None'):
		#If the column is full, dont change turns and return whoever turn it was and try again
		if(y_key == 115):
			return red_turn
		y_key -= 33

	if(red_turn):
		pygame.draw.circle(screen, red, (x_key, y_key), 17)
		board[x_key, y_key] = 'Red'
	else:
		pygame.draw.circle(screen, black, (x_key, y_key), 17)
		board[x_key, y_key] = 'Black'

	return not red_turn
#Checks to see if the user clicked in spot that would make them want to add a piece
def valid_click(pos):
	 x_start = 143
	 click = pos[0]
	 #Diameter of the circle in the gap of the image 
	 gap = 14
	 #Check if user clicked in the bounds of the board
	 if((pos[0] < 125) or (pos[0] > 374)):
	 	return False
	 if((pos[1] < 100) or (pos[1] > 300)):
	 	return False
	 #Check each gap
	 for i in range (0, 7):
	 	if (click > (x_start - gap) and (click < x_start + gap)):
	 		return True
	 	x_start += 36

	 return False
#Checks the status of the game TODO
def game_over_check(board):
	global winner
	
	#Check for pieces vertically for 4 in a row
	vertical = Logic.vertical_check(board) 
	if vertical != 'None':
		winner = vertical
		return True

	#Check for pieces horizontally 
	horizontal = Logic.horizontal_check(board)
	if horizontal != 'None':
		winner = horizontal
		return True

	#Check for pieces diagonally
	diagonal = Logic.diagonal_check(board)
	
	if diagonal != 'None':
		winner = diagonal
		return True
	#Checks if its a draw
	draw = Logic.draw_check(board)

	if draw != 'None':
		winner = 'Nobody'
		return True


	
pygame.init()
screen = pygame.display.set_mode((502, 500))
screen.fill((100,100,100))
screen.blit(get_image('images/connect_four_gridpng.png'), (125, 100))
done = False
red_turn = True
winner = 'None'

font = pygame.font.SysFont("arial", 32)
text = font.render("Test", True, (255, 0, 0))

black = (0, 0, 0)
red = (255, 0 ,0)
game_board = {}
create_game_board(game_board)






while not done:
	screen.fill((100,100,100), (150, 10, 200, 90) )

	
	
	if red_turn:
		text = font.render("Red turn", True, (200, 0, 0))
	else:
		text = font.render("Black turn", True, (0, 0, 0))
		


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			if valid_click(pygame.mouse.get_pos()):
				red_turn = add_piece(pygame.mouse.get_pos(), red_turn, game_board)
			


			
	if game_over_check(game_board):
		print('Game over ' + winner + ' wins')
		if winner is "Red":
			win_text = font.render(winner + " wins", True, (200, 0, 0))
		elif winner is 'Black':
			win_text = font.render(winner + " wins", True, (0, 0, 0))
		else:
			win_text = font.render("Its a draw", True, (50 ,50, 50))
		screen.blit(win_text, (300, 300))
		pygame.display.flip()
		pygame.time.delay(1000)
		done = True
	
	screen.blit(text, (180, 10))


	pygame.display.flip()
