#Adding Animation to the previous code
# Feels more and more interesting..
# In love with programming.
import curses
import time
screen = curses.initscr()
dims = screen.getmaxyx()
for z in range(dims[1]-12):
	screen.clear()
	screen.addstr(dims[0]/2,z,'Hello World!')
	screen.refresh()
	time.sleep(0.2)
screen.getch()
curses.endwin()