import random
import curses
from lista import Lista
from report import Report
foo =  open("/home/renato/Desktop/python/snake/snake_debug.txt","w+")
reportes = Report("/home/renato/Desktop/python/snake/")
score = Lista()
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw/4
snk_y = sh/2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
foo.write("Head: ({},{})".format(snake[0][0],snake[0][1])+"\n")
foo.write("body: ({},{})".format(snake[1][0],snake[1][1])+"\n")
foo.write("Tail: ({},{})".format(snake[2][0],snake[2][1])+"\n")
food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
    new_head = [0,0]
    foo.write("Current head: ({},{})".format(snake[0][0],snake[0][1])+"\n")
    if snake[0][0] in [0, sh]:
        new_head = [2, snake[0][1]]
        print(snake[0])
    elif snake[0][1] in [0, sw]:
        #new_head = [snake[0][0], 2]
        print(snake[0])
    elif snake[0] in snake[1:]:
        curses.endwin()
        reportes.scoreBoard_report(score)
        quit()
    else:
        new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
    	score.agregar(Lista(snake[0][0],snake[0][1]))
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
