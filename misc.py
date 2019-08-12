from lista import Lista
class Misc:
	def __init__(self,wind,a,b):
		self.win = wind
		self.pos_y = 4
		self.pos_x = 18
		self.max_x = a
		self.max_y = b
	def imprimir(self,content,inicio = False):
		another_aux = self.pos_x
		if(inicio):
			self.pos_x = 2
		if(self.pos_y == 15):
			self.clear_scr()
			self.pos_y = 4
		self.win.addstr(self.pos_y,self.pos_x, content)
		self.pos_x = another_aux
		self.pos_y+=1
	def print_centered(self, content):
		self.clear_scr()
		true_content = "<-	"+content+"	->"
		t_sh,t_sw = self.win.getmaxyx()
		true_pos = (t_sw - len(true_content))/4
		if(true_pos<1):
			true_pos = 1
		self.win.addstr(int(self.max_x/2),int(true_pos),true_content)
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
		try:
			f = open(name,"r")
			f1 = f.readlines()
			notFirst = False
			for content in f1:
				if(notFirst):
					new_user = content.strip()
					if( not vessel.has(new_user)):
						vessel.agregar(new_user)
				else:
					notFirst = True
			return True
		except:
			self.imprimir("An error has occurred while opening the file.",True)
			return False
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
		
