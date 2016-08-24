# Taking User Input using curses
# magic
# RationalScripts

import curses
import time
screen = curses.initscr()
curses.noecho()
dims = screen.getmaxyx()
q = -1
x,y =0,0
Vertical = 1
Horizontal = 1
while q != ord('q'):
	screen.clear()
	screen.addstr(y,x,'Hello World!')
	screen.move(dims[0] - 1,dims[1] - 1)
	screen.refresh()
	q = screen.getch()
	if q == ord('w') and y > 0 :
		y -= 1
	elif q == ord('s') and y < dims[0] - 1 :
		y += 1
	elif q == ord('a') and x > 0:
		x -= 1
	elif q == ord('d') and x < dims[1] - len('Hello World') - 1:
		x += 1
	if y == dims[0] - 1 and x == dims[1] - len('Hello World!'):
		if q == ord('s'):
			y -= 1
		elif q == ord('d'):
			x -= 1
curses.endwin()