def vertical_check(board):
	#Check rows verically for 4 in a row
	x_start = 143
	y_start = 280
	vertical_decrement = 33
	horizontal_increment = 36
	

	while(x_start <= 359):
		chain = 1
		start_color = board[x_start, y_start]

		if start_color == 'None':
			x_start+=horizontal_increment
			continue
			break
		

		for i in range (1, 6):
			next_color = board[x_start, (y_start - (vertical_decrement * i))]


			if next_color == start_color:
				chain+=1
			
				if chain is 4:
					return start_color

			elif next_color is 'None':
				break
				
			else:
				start_color = next_color
				chain = 1

		x_start+=horizontal_increment

	return 'None'

def horizontal_check(board):
	x_start = 143
	y_start = 280
	vertical_decrement = 33
	horizontal_increment = 36
	while(y_start >= 115):
		
		chain = 1
		start_color = board[x_start, y_start]
		

	
		for i in range (1, 7):
			next_color = board[(x_start + (horizontal_increment*i)), y_start]

			if next_color == start_color and next_color != 'None':
				chain+=1

				if chain is 4:
					return start_color

			elif next_color is 'None':
				chain = 0
				start_color = next_color
				continue
				

			else:
				start_color = next_color
				chain = 1
		
		y_start -= vertical_decrement

	return 'None'

def diagonal_check(board):
	x_start = 143
	y_start = 181
	
	
	vertical_increment = 33
	horizontal_increment = 36
	#Checks the board diagonal southeast to northwest
	while(x_start <= 251):

		chain = 1
		multiplier = 1
		start_color = board[x_start, y_start]
		current_y = y_start + (vertical_increment * multiplier)
		current_x = x_start + (horizontal_increment * multiplier)
		
		

		while(current_y <= 280 and current_x <= 359):
			
			
			next_color = board[current_x, current_y]

			if next_color == start_color and next_color != 'None':
				chain+=1

				if chain is 4:
					return start_color

			elif next_color is 'None':
				chain = 0
				start_color = next_color
				
				

			else:
				start_color = next_color
				chain = 1

			multiplier+=1
			current_y = y_start + (vertical_increment * multiplier)
			current_x = x_start + (horizontal_increment * multiplier)
			

		if (y_start == 115):
			x_start += horizontal_increment
		else:
			



			y_start -= vertical_increment


	x_start = 359
	y_start = 181
	#Checks the board diagonal going southwest to northeast
	while(x_start >= 251):

		chain = 1
		multiplier = 1
		start_color = board[x_start, y_start]
		current_y = y_start + (vertical_increment * multiplier)
		current_x = x_start - (horizontal_increment * multiplier)

		while(current_y <= 280 and current_x >= 143):

			next_color = board[current_x, current_y]

			if next_color == start_color and next_color != 'None':
				chain+=1

				if chain is 4:
					return start_color

			elif next_color is 'None':
				chain = 0
				start_color = next_color

			else:
				start_color = next_color
				chain = 1

			multiplier+=1
			current_y = y_start + (vertical_increment * multiplier)
			current_x = x_start - (horizontal_increment * multiplier)

		if (y_start == 115):
			x_start-= horizontal_increment
		else:
			y_start -= vertical_increment




	return 'None'		

def draw_check(board):
	x_start = 143
	y_start = 115

	for i in range(x_start, 360, 36):
		if board[i, y_start] == 'None':
			return 'None'

	return 'Draw'





