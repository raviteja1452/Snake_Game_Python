import curses
import time
import random

screen = curses.initscr()
#Snake Game
screen.keypad(1)
dims = screen.getmaxyx()
def game():
	screen.nodelay(1)
	head = [1,1]
	body = [head[:]]*5

	screen.border()
	direction = 0 
	# 0: Right 
	# 1: Down 
	# 2: Left
	# 3: Up
	gameover = False
	deadcell = body[-1]
	while not gameover:

		#Getting Directions
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
			gameover = True
		screen.move(dims[0]-1,dims[1]-1)
		screen.refresh()
		time.sleep(0.2)

game()
curses.endwin()


