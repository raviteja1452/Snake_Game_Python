# Taking User Input using curses
# magic
# RationalScripts

import curses
import time
screen = curses.initscr()
curses.noecho()
screen   .keypad(1)
dims = screen.getmaxyx()
q = -1
x,y =1,1
Vertical = 1
Horizontal = 1
screen.border()
while q != ord('q'):
	screen.addch(y,x,ord('$'))
	screen.move(dims[0] - 1,dims[1] - 1)
	screen.refresh()
	q = screen.getch()
	if q == curses.KEY_UP and y > 1 :
		screen.addch(y,x,' ')
		y -= 1
	elif q == curses.KEY_DOWN and y < dims[0] - 2 :
		screen.addch(y,x,' ')
		y += 1
	elif q == curses.KEY_LEFT and x > 1:
		screen.addch(y,x,' ')
		x -= 1
	elif q == curses.KEY_RIGHT and x < dims[1] - 2:
		screen.addch(y,x,' ')
		x += 1
curses.endwin()