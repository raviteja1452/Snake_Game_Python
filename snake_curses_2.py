import curses
import time
import random

startlength = 10
growlength = 5
speeds ={'Easy':0.1,'Medium':0.06,'Hard':0.04}
difficulty = 'Medium'
acceleration = True
screen = curses.initscr()
#Snake Game
screen.keypad(1)
dims = screen.getmaxyx()
def game():
	screen.clear()
	screen.nodelay(1)
	head = [1,1]
	body = [head[:]]*startlength

	screen.border()
	direction = 0 
	# 0: Right 
	# 1: Down 
	# 2: Left
	# 3: Up
	gameover = False
	foodmade = False
	deadcell = body[-1]
	while not gameover:

		#Getting Directions
		while not foodmade:
			y,x = random.randrange(1,dims[0]-1),random.randrange(1,dims[1] - 1)
			if screen.inch(y,x) == ord(' '):
				foodmade = True
				screen.addch(y,x,'#')
		action = screen.getch()
		if action == curses.KEY_UP and direction != 1:
			direction = 3
		elif action == curses.KEY_DOWN and direction != 3:
			direction = 1
		elif action == curses.KEY_RIGHT and direction != 2:
			direction = 0
		elif action == curses.KEY_LEFT and direction!= 0:
			direction = 2


		# Removing DeadCell
		if deadcell not in body:
			screen.addch(deadcell[0],deadcell[1],' ');
		# Adding Directions
		screen.addch(head[0],head[1],'$')

		#moving according to directions
		if direction == 0:
			head[1] += 1
		elif direction == 2:
			head[1] += -1
		elif direction == 1:
			head[0] += 1
		elif direction == 3:
			head[0]-= 1

		deadcell = body[-1]
		for z in range(len(body)-1,0,-1):
			body[z] = body[z-1]

		body[0] = head[:]

		if screen.inch(head[0],head[1]) != ord(' '):
			if screen.inch(head[0],head[1]) == ord('#'):
				# When food is found
				foodmade = False
				for z in range(growlength):
					body.append(body[-1])
			else:
				gameover = True
		screen.move(dims[0]-1,dims[1]-1)
		screen.refresh()
		if not acceleration:
			time.sleep(speeds[difficulty])
		else:
			time.sleep(15.*speeds[difficulty]/len(body))
	#After the game is over	
	screen.clear()
	screen.nodelay(0)
	message1 ='Game Over'
	message2 = 'You got '+str((len(body)-startlength)/growlength)+' points'
	message3 = 'Press Space to play again'
	message4 = 'Press Enter to Quit'
	message5 = 'Press M to go the menu'
	screen.addstr(dims[0]/2-2,(dims[1]-len(message1))/2,message1)
	screen.addstr(dims[0]/2-1,(dims[1]-len(message2))/2,message2)
	screen.addstr(dims[0]/2,(dims[1]-len(message3))/2,message3)
	screen.addstr(dims[0]/2+1,(dims[1]-len(message4))/2,message4)
	screen.addstr(dims[0]/2+2,(dims[1]-len(message5))/2,message5)
	screen.refresh()
	q = 0
	while q not in [32,10,77,109]:
		q = screen.getch()
		if q == 32:
			game()
		elif q in [77,109]:
			menu()	


def instructions():
	screen.clear()
	screen.nodelay(0)
	lines= ['Use the arrow keys to move','Don\'t run into the wall or the snake','','Press any key to go back']
	for z in range(len(lines)):
		screen.addstr((dims[0]-len(lines))/2+z,(dims[1]-len(lines[z]))/2,lines[z])
	screen.refresh()
	screen.getch()
	menu()

def gameoptions():
	global startlength,growlength,difficulty,acceleration
	screen.clear()
	selection = -1
	option = 0
	while selection < 4:
		screen.clear()
		graphics = [0]*5
		graphics[option] = curses.A_BOLD
		strings = ['Starting snake length: '+str(startlength),'Snake Growth rate: '+str(growlength),'Difficulty: '+difficulty,'Acceleration: '+str(acceleration),'Exit']
		for z in range(len(strings)):
			screen.addstr((dims[0]-len(strings))/2+z,(dims[1]-len(strings[z]))/2,strings[z],graphics[z])
		screen.refresh()
		action = screen.getch()
		if action == curses.KEY_UP:
			option = (option - 1)%5
		elif action == curses.KEY_DOWN:
			option = (option + 1) %5
		elif action == ord('\n'):
			selection = option
		if selection == 3:
			acceleration = not acceleration
		if selection < 4:
			selection = -1
	menu()
	

def menu():
	screen.clear()
	screen.nodelay(0)
	selection = -1
	option = 0
	while(selection < 0):
		graphics = [0]*5
		graphics[option] = curses.A_REVERSE
		screen.addstr(0,dims[1]/2-3,'Snake')
		screen.addstr(dims[0]/2-2,dims[1]/2-2,'Play',graphics[0])
		screen.addstr(dims[0]/2-1,dims[1]/2-6,'Instructions',graphics[1])
		screen.addstr(dims[0]/2,dims[1]/2-6,'Game Options',graphics[2])
		screen.addstr(dims[0]/2+1,dims[1]/2-5,'High Scores',graphics[3])
		screen.addstr(dims[0]/2+2,dims[1]/2-2,'Exit',graphics[4])
		screen.refresh()
		action = screen.getch()
		if action == curses.KEY_UP:
			option = (option - 1)%5
		elif action == curses.KEY_DOWN:
			option = (option + 1) %5
		elif action == ord('\n'):
			selection = option
	screen.clear()
	if selection == 0:
		game()
	elif selection == 1:
		instructions()
	elif selection == 2:
		gameoptions()




menu()
curses.endwin()


