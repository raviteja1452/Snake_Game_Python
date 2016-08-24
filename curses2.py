#curses Moving Strings

# Aligning Strings at the center of the screen
import curses
screen = curses.initscr()
# Here the coordinates are (Y,X)
dims = screen.getmaxyx()
screen.addstr(dims[0]/2,dims[1]/2-6, 'Hello World!')
screen.refresh()
screen.getch()
curses.endwin()