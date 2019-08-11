import random
import curses
from lista import Lista
from report import Report
class snake_game:
	def __init__(self,origin,max_x,max_y,o_window):
		self.reportes = Report("")
		self.foo =  open("true_snake_debug.txt","w+")
		self.score = Lista()
		self.sh, self.sw = o_window.getmaxyx()
		self.w = o_window
		self.w.keypad(1)
		self.w.timeout(100)
		self.snake = origin
		self.food = Lista(self.sh/2, self.sw/2)
		self.key = curses.KEY_RIGHT
	def get_new_snake(self):
		n_snake = Lista()
		snk_x = self.sw/4
		snk_y = self.sh/2
		n_snake.agregar(Lista(snk_y, snk_x-2))
		n_snake.agregar(Lista(snk_y, snk_x-1))
		n_snake.agregar(Lista(snk_y, snk_x))
		return n_snake	
	def jugar(self,resume):
		self.w.keypad(1)
		self.w.timeout(100)
		self.snake = resume
		self.key = curses.KEY_RIGHT
		self.foo.write("Trying to paint food in: ({},{})".format(int(self.food.head.content), int(self.food.tail.content)))
		self.w.addch(int(self.food.head.content), int(self.food.tail.content), curses.ACS_PI)
		while True:
			next_key = self.w.getch()
			self.key = self.key if next_key == -1 else next_key
			new_head = Lista(18,18)
			self.foo.write("Current head: "+self.snake.head.content.snake_body()+"\n")
			if self.snake.head.content.head.content == 0:
				new_head = Lista(self.sh-1, self.snake.head.content.tail.content)
			elif self.snake.head.content.head.content == self.sh:
				new_head = Lista(1,self.snake.head.content.tail.content)
			elif self.snake.head.content.tail.content == 0:
				new_head = Lista(self.snake.head.content.head.content, self.sw-1)
			elif self.snake.head.content.tail.content == self.sw:
				new_head = Lista(self.snake.head.content.head.content,1)
			elif self.snake.is_in_itself():
				if(self.snake.should_be_reversed()):
					self.snake.reverse_content()
					self.foo.write("Snake has been reversed.")
					new_head = Lista(self.snake.head.content.head.content, self.snake.head.content.tail.content)
				else:
					another_result = Lista()
					another_result.agregar(self.score)
					another_result.agregar(self.snake)
					another_result.agregar(False)
					self.foo.write("Finished Excecution")
					return another_result
			else:
				new_head = Lista(self.snake.head.content.head.content, self.snake.head.content.tail.content)
			if self.key == curses.KEY_DOWN:
				new_head.head.content += 1
			if self.key == curses.KEY_UP:
				new_head.head.content -= 1
			if self.key == curses.KEY_LEFT:
				new_head.tail.content -= 1
			if self.key == curses.KEY_RIGHT:
				new_head.tail.content += 1
			if self.key == 8:
				true_result = Lista()
				true_result.agregar(self.score)
				true_result.agregar(self.snake)
				true_result.agregar(True)
				return true_result
			self.foo.write("New head: "+new_head.snake_body())
			self.snake.agregar(new_head)
			borders = Lista()
			borders.agregar(0)
			borders.agregar(self.sh)
			borders.agregar(self.sw)
			if self.snake.head.content.comparar(self.food):
				self.score.agregar(Lista(self.snake.head.content.head.content,self.snake.head.content.tail.content))
				self.food = None
				while self.food is None:
					nf = Lista(random.randint(1, self.sh-1),random.randint(1, self.sw-1))
					self.food = nf if not self.snake.is_inside(nf) else None
				self.w.addch(self.food.head.content, self.food.tail.content, curses.ACS_PI)
			else:
				true_tail = self.snake.popElement()
				self.foo.write("Removed tail: "+true_tail.snake_body())
				if( not borders.has(true_tail.head.content) and not borders.has(true_tail.tail.content)):
					self.w.addch(int(true_tail.head.content), int(true_tail.tail.content), ' ')
			if( not borders.has(self.snake.head.content.head.content) and not borders.has(self.snake.head.content.tail.content)):
				self.w.addch(int(self.snake.head.content.head.content), int(self.snake.head.content.tail.content), curses.ACS_CKBOARD)
"""s = curses.initscr()
curses.curs_set(0)
tsh, tsw = s.getmaxyx()
wii = curses.newwin(tsh, tsw, 0, 0)
tsnk_x = tsw/4
tsnk_y = tsh/2
t_snake = Lista()
t_snake.agregar(Lista(tsnk_y, tsnk_x-2))
t_snake.agregar(Lista(tsnk_y, tsnk_x-1))
t_snake.agregar(Lista(tsnk_y, tsnk_x))
juego = snake_game(t_snake,tsnk_x,tsnk_y,wii)
juego.jugar(t_snake)
"""
