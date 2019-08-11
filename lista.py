import inspect
f= open("/home/renato/Desktop/python/snake/debug.txt","w+")
class Node:
	def __init__(self, algo):
		self.content = algo
		self.next = None
		self.prev = None
	def snake_node(self,indice):
		return "s{}".format(indice)+" [label=\"{<ref0> | <data> "+self.content.snake_body()+" | <ref>  }\"];"
	def toBody(self):
		return self.content
class Lista:
	def __init__(self, a = None, b = None):
		if(a is None and b is None):
			self.head = None
			self.tail = None
			self.size = 0
		else:
			self.head = Node(a)
			self.tail = Node(b)
			self.head.next = self.tail
			self.tail.prev = self.head
			self.size = 2
		self.iter = 0
	def snake_body(self):
		if(self.head is not None and self.tail is not None):
			return "({},{})".format(self.head.content,self.tail.content)
	def comparar(self, other):
		aux = self.head
		aux1 = other.head
		if(self.size == other.size):
			while(aux is not None):
				if(aux.content != aux1.content):
					return False
				aux = aux.next
				aux1 = aux1.next
			return True
		return False
	def reverse_content(self):
		vessel = Lista()
		aux = self.head
		while(aux is not None):
			vessel.agregar(aux.content)
			aux = aux.next
		self.head = vessel.head
		self.tail = vessel.tail
		self.size = vessel.size
	def should_be_reversed(self):
		if(self.head is not None):
			if(self.head.next is not None):
				if(self.head.next.next is not None):
					if(self.head.content.comparar(self.head.next.next.content)):
						return True
		return False
	def is_in_itself(self):
		aux_head = self.head.content
		aux = self.head
		isNotHead = False
		while(aux is not None):
			if(isNotHead):
				if(aux.content.comparar(aux_head)):
					return True
			else:
				isNotHead = True
			aux = aux.next
		return False
	def is_inside(self,other):
		aux = self.head
		while(aux is not None):
			if(aux.content.comparar(other)):
				return True
			aux = aux.next
		return False
	def popElement(self):
		if(self.head is None):
			return None
		if(self.size == 1):
			self.head = self.tail = None
			self.size = 0
			return None
		aux = self.tail
		self.tail.prev.next = None
		self.tail = self.tail.prev
		aux.prev = None
		self.size -= 1
		return aux.content
	def has(self,other):
		global f
		f.write("Searching for: {}".format(other)+"\n")
		f.write("In list: "+"\n")
		aux = self.head
		while(aux is not None):
			f.write("{}".format(aux.content)+"\n")
			if(aux.content == other):
				f.write("Found: {}".format(aux.content)+"\n")
				return True
			aux = aux.next
		return False
	def agregar(self,algo):
		if(self.head is None):
			self.head = self.tail = Node(algo)
		else:
			aux = Node(algo)
			self.head.prev = aux
			aux.next = self.head
			self.head = aux
		self.size +=1
	def derecha(self):
		if(self.head is None):
			return
		else:
			true_aux = self.getNode(self.iter)
			if(true_aux is None):
				return
			else:
				if(true_aux.next is None):
					self.iter = 0
				else:
					self.iter += 1
	def izquierda(self):
		if(self.head is None):
			return
		else:
			aux = self.getNode(self.iter)
			if(aux is None):
				return
			else:
				if(aux.prev is None):
					self.iter = self.size-1
				else:
					self.iter -= 1				
	def contains(self,algo):
		auxiliar = self.head
		while(auxiliar is not None):
			if(algo == auxiliar.content):
				return True
			auxiliar = auxiliar.next
		return False
	def imprimir(self,agregarIndice=False):
		if(agregarIndice):
			if(self.head is None):
				print("No users have been found.")
				return
			c = 1
			auxiliar = self.head
			while(auxiliar is not None):
				print("{}. ".format(c)+auxiliar.content)
				c+=1
				auxiliar = auxiliar.next
			#print("{}. Salir".format(c))
		else:
			auxiliar = self.head
			while(auxiliar is not None):
				print(auxiliar.content)
				auxiliar = auxiliar.next
	def getElement(self, indice):
		c = 0
		aux = self.head
		while(aux is not None):
			if(indice == c):
				return aux.content
			c += 1
			aux = aux.next
		return None
	def getNode(self, indice):
		c = 0
		aux = self.head
		while(aux is not None):
			if(indice == c):
				return aux
			c += 1
			aux = aux.next
		return None
	def getUser(self):
		aux = self.getElement(self.iter)
		if(aux is None):
			return "No users have been found."
		else:
			return aux
	def enqueue(self, algo,resize = True):
		if(self.size == 10 and resize):
			self.unqueue()
		if(self.head is None):
			self.head=self.tail=Node(algo)
		else:
			aux = Node(algo)
			self.tail.next = aux
			aux.prev = self.tail
			self.tail = aux
		self.size += 1
	def unqueue(self):
		auxiliar = self.head
		if(self.head is None):
			self.iter = 0
			return None
		if(self.head.next is None):
			self.head = self.tail = None
			self.size = 0
			self.iter = 0
			return auxiliar
		else:
			self.head.next.prev = None
			self.head = self.head.next
			auxiliar.next = None
			self.size -= 1
			self.iter = 0
			return auxiliar
	def __eq__(self,other):
		if(isinstance(other, Lista)):
			auxiliar = self.head
			auxiliar2 = other.head
			if(auxiliar.size==auxiliar2.size):
				while(auxiliar is not None):
					if(auxiliar.content != auxiliar2.content):
						return False
					auxiliar = auxiliar.next
					auxiliar2 = auxiliar2.next
				return True
			return False
		else:
			return False

'''prueba = Lista()
prueba.agregar(5)
prueba.agregar(6)
prueba.agregar(7)
prueba.agregar(8)
prueba.agregar("hola")
prueba.agregar(9)
prueba.agregar("mundo")

prueba.imprimir()
prueba2 = Lista("Marth","Julius")
prueba2.imprimir()
if(prueba.contains(11)):
	print("algo esta mal")
else:
	print("el contains funciona!")
if(prueba.contains("hola")):
	print("sip, solo queria estar seguro")
else:
	print("Nope, something went wrong...")
'''
