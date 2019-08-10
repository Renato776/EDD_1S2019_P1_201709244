from lista import Lista
class Misc:
	def __init__(self,wind,a,b):
		self.win = wind
		self.pos_y = 4
		self.pos_x = 18
		self.max_x = a
		self.max_y = b
	def imprimir(self,content):
		if(self.pos_y == 15):
			self.clear_scr()
			self.pos_y = 4
		self.win.addstr(self.pos_y,self.pos_x, content)
		self.pos_y+=1
	def print_centered(self, content):
		self.clear_scr()
		self.win.addstr(int(self.max_x/2),int(self.max_y/4),content)
	def clear_scr (self):
		self.win.clear()
		self.win.border(0)
	def fixed_print(self,content):
		self.win.addstr(self.pos_y,self.pos_x, content)
	def print_title(self,content):
		self.win.addstr(int(self.max_x/6),int(self.max_y/6),content)
	def print_row(self,a,b):
		if(self.pos_y == 15):
			self.clear_scr()
			self.pos_y = 4
		self.win.addstr(self.pos_y,int(self.max_x/4), a)
		self.win.addstr(self.pos_y,int((self.max_x/4)*3+15), b)
		self.pos_y+=1
	def reset_pos(self):
		self.pos_y = 4
	def bulk_loading(self,name,vessel):
		f = open(name,"r")
		f1 = f.readlines()
		notFirst = False
		for content in f1:
			if(notFirst):
				vessel.agregar(content)
			else:
				notFirst = True
	def getString(self):
		cadena = ""
		key = self.win.getch()
		while key!=10:
			if(key == 8):
					cadena = cadena[:-1]
					self.fixed_print(cadena)
			else:
				try:
					letra = chr(key)
					cadena = cadena + letra
					self.fixed_print(cadena)
				except:
					cadena = cadena
			key = self.win.getch()
		return cadena
		
