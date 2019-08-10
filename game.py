import curses #import the curses library
import time
from lista import Lista
from misc import Misc
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
misc = None
max_x = 20
max_y = 60
usuarios = Lista()
scoreBoard = Lista()
usuario = None
def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.addstr(7,21, '1. Play')             #paint option 1
    win.addstr(8,21, '2. Scoreboard')       #paint option 2
    win.addstr(9,21, '3. User Selection')   #paint option 3
    win.addstr(10,21, '4. Reports')         #paint option 4
    win.addstr(11,21, '5. Bulk Loading')    #paint option 5
    win.addstr(12,21, '6. Exit')            #paint option 6
    win.timeout(-1)                         #wait for an input thru the getch() function

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,int(x_start),var)           #paint the title on the screen

def wait_esc(win):
    key = window.getch()
    misc.imprimir("pressed key's constant: {}".format(key))
    while key!=27:
        key = window.getch()
        if(key == 49):
        	misc.print_centered("centrado")
        else:
        	misc.imprimir("pressed key's constant: {}".format(key))
def user_selection_header():
	global usuario
	misc.print_title("Usuario: ")
	us = usuarios.getUser()
	misc.print_centered(us)
	if(us == "No users have been found." ):
		usuario = None
	else:
		usuario = us 
def user_selection():
	global usuario
	user_selection_header()
	key = 28
	while key!=27:
		key = window.getch()
		if(key == 261):
			usuarios.derecha()
			us = usuarios.getUser()
			misc.print_centered(us)
			if(us == "No users have been found." ):
				usuario = None
			else:
				usuario = us 
				misc.print_centered(us)
		elif(key == 260):
			usuarios.izquierda()
			us = usuarios.getUser()
			misc.print_centered(us)
			if(us == "No users have been found." ):
				usuario = None
			else:
				usuario = us 
			misc.print_centered(us)
		elif(key == 8):
			misc.clear_scr()
			misc.print_title("Creacion de Usuario:")
			newUser = misc.getString()
			#misc.imprimir("Usuario: "+newUser+" Ha sido creado con exito.")
			usuarios.agregar(newUser)
			usuario = newUser
			misc.clear_scr()
			user_selection_header()

def score_board():
	misc.reset_pos()
	misc.print_row("User","Score")
	aux = scoreBoard.tail
	key = 0
	while(aux is not None):
		if(aux.content is not None):
			misc.print_row(aux.content.head.content,aux.content.tail.content)
			aux = aux.prev
	while key!=27:
		key = window.getch()	
stdscr = curses.initscr() #initialize console
window = curses.newwin(max_x,max_y,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)		
misc = Misc(window,max_x,max_y)

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        paint_title(window, ' PLAY ')
        misc.imprimir("About to check usuario")
        if(usuario is not None):
        	misc.imprimir("intentando agregar Usuario: "+usuario)
        	scoreBoard.agregar(Lista(usuario,"20"))
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' SCOREBOARD ')
        score_board()
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' USER SELECTION ')
        user_selection()
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' REPORTS ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' BULK LOADING ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state
