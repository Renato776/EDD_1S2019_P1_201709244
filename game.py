import curses #import the curses library
import time
from lista import Lista
from misc import Misc
from snake import snake_game
from report import Report
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
misc = None
max_x = 20
max_y = 60
usuarios = Lista()
scoreBoard = Lista()
true_stack = Lista()
usuario = None
reportes = Report("")
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
			if( not usuarios.has(newUser)):
				usuarios.agregar(newUser)
			usuario = newUser
			misc.clear_scr()
			user_selection_header()
def bulk_loading():
	#misc.win.addstr(misc.pos_y,3, "Type the name of the archive you'd like to load:")
	#misc.pos_y+=1
	misc.imprimir("Type the name of the archive you'd like to load:",True)
	target = misc.getString()
	success = misc.bulk_loading(target,usuarios)
	if(success):
		misc.imprimir("All users have been registrated successfully!",True)
def score_board():
	misc.reset_pos()
	misc.print_row("User","Score")
	aux = scoreBoard.head
	key = 0
	while(aux is not None):
		if(aux.content is not None):
			misc.print_row(aux.content.head.content,aux.content.tail.content)
			aux = aux.next
	while key!=27:
		key = window.getch()	
def report_selection(t_window):
	misc.reset_pos()
	misc.clear_scr()
	paint_title(t_window,"Report Selection")
	misc.imprimir("1. Snake Report")
	misc.imprimir("2. Score Report")
	misc.imprimir("3. Score Board Report")
	misc.imprimir("4. Users Report")
	misc.imprimir("5. Go Back.")
	key = 0
	while key!=53:
		key = window.getch()
		if(key == 49):
			reportes.snake_report(true_snake)
			misc.imprimir("Snake report generated successfully!")
		elif(key==50):
			reportes.stack_report(true_stack)
			misc.imprimir("Score report generated successfully!")
		elif(key==51):
			reportes.scoreBoard_report(scoreBoard)
			misc.imprimir("Score Board report generated successfully!")
		elif(key==52):
			reportes.users_report(usuarios)
			misc.imprimir("Users Report generated successfully!")
	misc.clear_scr()
stdscr = curses.initscr() #initialize console
window = curses.newwin(max_x,max_y,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)		
misc = Misc(window,max_x,max_y)
true_game = snake_game(None,max_x,max_y,window,usuario)
true_snake = true_game.get_new_snake()
pausa = False
keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
		misc.clear_scr()
		paint_title(window, ' PLAY ')
		if(usuario is None):
			misc.clear_scr()
			misc.print_title("Creacion de Usuario:")
			newUser = misc.getString()
			usuarios.agregar(newUser)
			usuario = newUser
			misc.clear_scr()
			paint_title(window, ' PLAY ')
		true_game.player = usuario
		valores = None
		if(pausa):
			valores = true_game.jugar(true_snake)
		else:
			valores = true_game.jugar(true_game.get_new_snake())
		pausa = valores.head.content
		if(pausa):
			true_snake = valores.head.next.content
			reportes.snake_report(true_snake)
			reportes.stack_report(valores.tail.content)
			true_stack = valores.tail.content
		else:
			true_snake = valores.head.next.content
			reportes.snake_report(true_snake)
			reportes.stack_report(valores.tail.content)
			true_stack = valores.tail.content
			scoreBoard.enqueue(Lista(usuario,"{}".format(valores.tail.content.size)))	
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
        report_selection(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' BULK LOADING ')
        bulk_loading()
        key = window.getch()
        paint_menu(window)
        keystroke=-1
    elif(keystroke==54):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state
