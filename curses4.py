import curses
import time
screen = curses.initscr()
screen.nodelay(1)
dims = screen.getmaxyx()
q = -1
x,y =0,0
Vertical = 1
Horizontal = 1
while q < 0:
	screen.clear()
	screen.addstr(y,x,'Hello World!')
	screen.refresh()
	y += Vertical
	x += Horizontal
	if y == dims[0] - 1:
		Vertical = -1
	elif y == 0:
		Vertical = 1
	if x == dims[1] - len('Hello World!') - 1:
		Horizontal = -1
	elif x == 0:
		Horizontal = 1
	q = screen.getch()
	time.sleep(0.05)
screen.getch()
curses.endwin()