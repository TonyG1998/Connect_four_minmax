import pygame
import os

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
		for j in range(0, 6):
			board[x_start, y_start] = "None"
			y_start-=33
		x_start+=36

def add_piece(pos, red_turn):
	global black
	global red
	pygame.draw.circle(screen, red, pygame.mouse.get_pos(), 17)

	return not red_turn
#Checks to see if the user clicked in spot that would make them want to add a piece
def valid_click(pos):
	 x_start = 143
	 click = pos[0]
	 #Diameter of the circle in the gap of the image 
	 gap = 12
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

pygame.init()
screen = pygame.display.set_mode((502, 500))
screen.fill((100,100,100))
screen.blit(get_image('.\\images\\connect_four_gridpng.png'), (125, 100))
done = False
red_turn = True

black = (0, 0, 0)
red = (255, 0 ,0)
game_board = {}
create_game_board(game_board)






while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(valid_click(pygame.mouse.get_pos()))
			if valid_click(pygame.mouse.get_pos()):
				red_turn = add_piece(pygame.mouse.get_pos(), red_turn)

			
	
	



	pygame.display.flip()
