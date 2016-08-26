import curses
import time
import random

screen = curses.initscr()
#Snake Game
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

	while not gameover:
		screen.addch(head[0],head[1],'$')
		if direction == 0:
			head[1] += 1
		elif direction == 2:
			head[1] += -1
		elif direction == 1:
			head[0] += 1
		elif direcion == 3:
			head[0]-= 1

		deadcell = body[-1]
		for z in range(len(body)-1,0,-1):
			body[z] = body[z-1]

		if screen.inch(head[0],head[1]) != ord(' '):
			gameover = True
		screen.refresh()
		time.sleep(0.1)

game()
curses.endwin()


