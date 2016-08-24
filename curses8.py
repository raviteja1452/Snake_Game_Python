#rationalscripts
import curses
import time
message = raw_input('Enter messge desired: ')
print message
screen = curses.initscr()
curses.start_color()
curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
curses.init_pair(3,curses.COLOR_RED,curses.COLOR_BLACK)
g = 1
bold = 0
reverse = 0
curses.noecho()
screen.nodelay(1)
dims = screen.getmaxyx()
q = -1
x,y =0,0
Vertical = 1
Horizontal = 1
b = [curses.A_NORMAL,curses.A_BOLD]
r = [curses.A_NORMAL,curses.A_REVERSE]
while q < 0 or q in range(49,52) or q in [98,114]:
	screen.clear()
	if q in range(49,52):
		g = int(chr(q))
	elif q == 98:
		bold = (bold + 1)%2
	elif q == 114:
		reverse = (reverse + 1)%2
	screen.addstr(y,x,message,curses.color_pair(g)|b[bold]|r[reverse])
	screen.refresh()
	y += Vertical
	x += Horizontal
	if y == dims[0] - 1:
		Vertical = -1
	elif y == 0:
		Vertical = 1
	if x == dims[1] - len(message) - 1:
		Horizontal = -1
	elif x == 0:
		Horizontal = 1
	q = screen.getch()
	time.sleep(0.05)
screen.getch()
curses.endwin()