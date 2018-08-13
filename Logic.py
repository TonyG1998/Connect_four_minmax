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
		

		if start_color != 'None':
			for i in range (1, 7):
				next_color = board[(x_start + (horizontal_increment*i)), y_start]

				if next_color == start_color:
					chain+=1

					if chain is 4:
						return start_color

				elif next_color is 'None':
					chain = 0
					continue
					

				else:
					start_color = next_color
					chain = 1
		
		y_start -= vertical_decrement

	return 'None'





