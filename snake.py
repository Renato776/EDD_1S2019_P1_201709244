import random
import curses
from lista import Lista
from report import Report
class snake_game:
	def __init__(self,origin,max_x,max_y,o_window,jugador):
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
		self.level = 0
		self.is_poison = False
		self.food_symbol = "+"
		self.obstacles = Lista()
		self.player = jugador
		self.difficulty = 80
		self.thereshold = 15
		try:
			fu = open("config.ren","r")
			f1 = fu.readlines()
			c = 0
			for content in f1:
				if(c==0):
					self.difficulty = int(content.strip())
				elif(c==1):
					self.thereshold = int(content.strip())
				c+=1
		except:
			self.difficulty = 80
	def get_new_snake(self):
		n_snake = Lista()
		snk_x = self.sw/4
		snk_y = self.sh/2
		n_snake.agregar(Lista(snk_y, snk_x-2))
		n_snake.agregar(Lista(snk_y, snk_x-1))
		n_snake.agregar(Lista(snk_y, snk_x))
		return n_snake
	def make_obstacle(self):
		true_new_obs = None
		while(true_new_obs is None):
			new_obs = Lista()
			o_x = random.randint(1, self.sw-1)
			o_y = random.randint(1, self.sh-1)
			new_obs.agregar(Lista(o_y,o_x))
			new_obs.agregar(Lista(o_y,o_x+1))
			new_obs.agregar(Lista(o_y,o_x+2))
			true_new_obs = new_obs if self.validate_obs(new_obs) else None
		self.obstacles.agregar(true_new_obs)
	def validate_obs(self, triada):
		aux = triada.head
		t_borders = Lista()
		t_borders.agregar(0)
		t_borders.agregar(self.sh)
		t_borders.agregar(self.sw)
		t_borders.agregar(self.sw+1)
		t_borders.agregar(self.sw+2)
		t_borders.agregar(self.sh)
		t_borders.agregar(self.sh+1)
		t_borders.agregar(self.sh+2)
		while(aux is not None):
			if(self.snake.is_inside(aux.content)):
				return False
			if( t_borders.has(aux.content.head.content) or t_borders.has(aux.content.tail.content)):
				return False
			if(self.food.comparar(aux.content)):
				return False
			if(self.obstacles.is_inside(aux.content)):
				return False
			aux = aux.next
		return True
	def calculate_obstacles(self):
		if(self.level == 1):
			self.make_obstacle()
		self.make_obstacle()
		#while(c<self.level):
		#	self.make_obstacle()
		#	c+=1
	def paint_obstacles(self):
		aux = self.obstacles.head
		while(aux is not None):
			"""self.foo.write("Trying to paint obstacle at: ")
			self.foo.write(aux.__class__.__name__+"\n")
			self.foo.write(aux.content.__class__.__name__+"\n")
			self.foo.write(aux.content.head.__class__.__name__+"\n")
			self.foo.write(aux.content.head.content.__class__.__name__+"\n")
			self.foo.write(aux.content)
			self.foo.write(aux.content)"""
			aux1 = aux.content.head
			while(aux1 is not None):
				self.w.addch(int(aux1.content.head.content), int(aux1.content.tail.content), "^")
				aux1 = aux1.next	
			aux = aux.next
	def is_in_obstacle(self):
		aux = self.snake.head.content
		aux1 = self.obstacles.head
		while(aux1 is not None):
			if(aux1.content.is_inside(aux)):
				return True
			aux1 = aux1.next
		return False
	def food_is_in_obstacle(self, nf):
		aux1 = self.obstacles.head
		while(aux1 is not None):
			if(aux1.content.is_inside(nf)):
				return True
			aux1 = aux1.next
		return False
	def back_to_default(self):
		self.level = 0
		self.obstacles = Lista()
		self.score = Lista()
		self.player = ""
	def jugar(self,resume):
		self.w.keypad(1)
		self.w.timeout(100)
		self.snake = resume
		self.key = curses.KEY_RIGHT
		self.foo.write("Trying to paint food in: ({},{})".format(int(self.food.head.content), int(self.food.tail.content)))
		self.w.addch(int(self.food.head.content), int(self.food.tail.content), self.food_symbol)
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
					self.back_to_default()
					self.foo.write("Finished Excecution")
					return another_result
			elif self.is_in_obstacle():
				another_result = Lista()
				another_result.agregar(self.score)
				another_result.agregar(self.snake)
				another_result.agregar(False)
				self.back_to_default()
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
				if(self.is_poison):
					self.score.unqueue()
					true_tail = self.snake.popElement()
					if( not borders.has(true_tail.head.content) and not borders.has(true_tail.tail.content)):
						self.w.addch(int(true_tail.head.content), int(true_tail.tail.content), ' ')
					absolute_tail = self.snake.popElement()
					if( not borders.has(absolute_tail.head.content) and not borders.has(absolute_tail.tail.content)):
						self.w.addch(int(absolute_tail.head.content), int(absolute_tail.tail.content), ' ')
				else:
					self.score.agregar(Lista(self.snake.head.content.head.content,self.snake.head.content.tail.content))
					if((self.score.size % self.thereshold) == 0):
						self.level += 1
						self.calculate_obstacles()
						self.paint_obstacles()
				self.food = None
				new_type = random.randint(1, 100)
				if(new_type <= self.difficulty):
					while self.food is None:
						nf = Lista(random.randint(1, self.sh-1),random.randint(1, self.sw-1))
						self.food = nf if (not self.snake.is_inside(nf)) and (not self.food_is_in_obstacle(nf)) else None
					self.is_poison = False
					self.food_symbol = "+"
				else:
					while self.food is None:
						nf = Lista(random.randint(1, self.sh-1),random.randint(1, self.sw-1))
						self.food = nf if (not self.snake.is_inside(nf)) and ( not self.food_is_in_obstacle(nf)) else None
					self.is_poison = True
					self.food_symbol = "*"
				self.w.addch(self.food.head.content, self.food.tail.content, self.food_symbol)
			else:
				true_tail = self.snake.popElement()
				self.foo.write("Removed tail: "+true_tail.snake_body())
				if( not borders.has(true_tail.head.content) and not borders.has(true_tail.tail.content)):
					self.w.addch(int(true_tail.head.content), int(true_tail.tail.content), ' ')
			if( not borders.has(self.snake.head.content.head.content) and not borders.has(self.snake.head.content.tail.content)):
				self.w.addch(int(self.snake.head.content.head.content), int(self.snake.head.content.tail.content), curses.ACS_CKBOARD)
			self.w.addstr(0,5, "User: "+self.player)
			self.w.addstr(0,self.sw-10,"Score: {}".format(self.score.size))
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
