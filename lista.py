import inspect
class Node:
	def __init__(self, algo):
		self.content = algo
		self.next = None
		self.prev = None
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
	
	def agregar(self,algo):
		if(self.head is None):
			self.head = self.tail = Node(algo)
		else:
			aux = Node(algo)
			self.head.prev = aux
			aux.next = self.head
			self.head = aux
		self.size +=1
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
	def enqueue(self, algo):
		if(self.size == 10):
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
			return None
		if(self.head.next is None):
			self.head = self.tail = None
			self.size = 0
			return auxiliar
		else:
			self.head.next.prev = None
			self.head = self.head.next
			auxiliar.next = None
			self.size -= 1
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
