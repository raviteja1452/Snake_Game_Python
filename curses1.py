#print Hello World using Curses\
#Dependancy Curses Libraray

import curses
#import curses library

screen = curses.initscr()
#screen variable is initialized to curses screen

screen.addstr(0,0,'Hello World!')

screen.refresh()

#wait till we enter a char from keyboard
screen.getch()

#end curses window object
curses.endwin()