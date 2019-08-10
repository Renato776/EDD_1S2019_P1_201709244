import random
import curses
from lista import Lista
from report import Report
reportes = Report("/home/renato/Desktop/python/snake/")
foo =  open("/home/renato/Desktop/python/snake/true_snake_debug.txt","w+")
score = Lista()
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = Lista()
snake.agregar(Lista(snk_y, snk_x-2))
snake.agregar(Lista(snk_y, snk_x-1))
snake.agregar(Lista(snk_y, snk_x))
food = Lista(sh/2, sw/2)
w.addch(int(food.head.content), int(food.tail.content), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
    new_head = Lista(0,0)
    foo.write("Current head: "+snake.head.content.snake_body()+"\n")
    if snake.head.content.head.content == 0:
        new_head = Lista(sh-1, snake.head.content.tail.content)
    elif snake.head.content.head.content == sh:
    	new_head = Lista(1,snake.head.content.tail.content)
    elif snake.head.content.tail.content == 0:
        new_head = Lista(snake.head.content.head.content, sw-1)
    elif snake.head.content.tail.content == sw:
    	new_head = Lista(snake.head.content.head.content,1)
    elif snake.is_in_itself():
        #curses.endwin()
        reportes.scoreBoard_report(score)
        #quit()
    else:
        new_head = Lista(snake.head.content.head.content, snake.head.content.tail.content)

    if key == curses.KEY_DOWN:
        new_head.head.content += 1
    if key == curses.KEY_UP:
        new_head.head.content -= 1
    if key == curses.KEY_LEFT:
        new_head.tail.content -= 1
    if key == curses.KEY_RIGHT:
        new_head.tail.content += 1
	foo.write("New head: "+new_head.snake_body())
    snake.agregar(new_head)
    borders = Lista()
    borders.agregar(0)
    borders.agregar(sh)
    borders.agregar(sw)

    if snake.head.content.comparar(food):
    	score.agregar(Lista(snake.head.content.head,snake.head.content.tail))
        food = None
        while food is None:
            nf = Lista(random.randint(1, sh-1),random.randint(1, sw-1))
            food = nf if not snake.is_inside(nf) else None
        w.addch(food.head.content, food.tail.content, curses.ACS_PI)
    else:
        true_tail = snake.popElement()
        foo.write("Removed tail: "+true_tail.snake_body())
        if( not borders.has(true_tail.head.content) and not borders.has(true_tail.tail.content)):
        	w.addch(int(true_tail.head.content), int(true_tail.tail.content), ' ')
	if( not borders.has(snake.head.content.head.content) and not borders.has(snake.head.content.tail.content)):
		w.addch(int(snake.head.content.head.content), int(snake.head.content.tail.content), curses.ACS_CKBOARD)
