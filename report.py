from lista import Lista
from subprocess import call
import pydot
import os
class Report:
	def __init__(self,dir):
		self.direccion = dir
		self.header = "digraph foo { rankdir=LR; node [shape=record];"
		self.stack_header = "digraph foo {rankdir=TB; node [shape=record];"
	def getImage(self,name):
		#cmd = "dot -Tpng "+"/home/renato/Desktop/python/snake/"+name+".dot"+" -o "+"/home/renato/Desktop/python/snake/"+name+".png"
		#os.system(cmd)
		#call('dot -Tpng /home/renato/Desktop/python/snake/'+name+'.dot -o /home/renato/Desktop/python/snake/'+name+'.png', shell=True)
		#call('touch /home/renato/Desktop/python/snake/'+name+'.txt',shell = True)
		os.system('dot -Tpng /home/renato/Desktop/python/snake/'+name+'.dot -o /home/renato/Desktop/python/snake/'+name+'.png')
	def scoreBoard_report(self,scoreBoard):
		aux = scoreBoard.head
		resultado = self.header+"\n"+"n2[label = \"null\"]"+"\n"
		c = 0
		while(aux is not None):
			resultado = resultado + "s{}".format(c) +"[label=\"{ <data> "+aux.content.snake_body()+" | <ref>  }\"];"+"\n"
			if(aux.next is not None):
				resultado = resultado + "s{}".format(c)+":ref -> s{} [arrowhead=vee, tailclip=false, arrowtail = vee];".format(c+1)+"\n"
			else:
				resultado = resultado + "s{}".format(scoreBoard.size-1)+":ref -> n2      [arrowhead=vee, tailclip=false,arrowtail = vee];" + "\n"
			c += 1
			aux = aux.next
		resultado = resultado +"}"
		grafos = pydot.graph_from_dot_data(resultado)
		(g,)=grafos
		g.write_jpg('scoreBoard.jpg')
		os.system('scoreBoard.jpg')
	def users_report(self,usuarios):
		aux = usuarios.head
		c = 0
		resultado = self.header+"\n"
		while(aux is not None):
			resultado = resultado + "s{}".format(c) +"[label=\"{<ref0> | <data> "+aux.toBody()+" | <ref>  }\"];"+"\n"
			if(aux.next is not None):
				resultado = resultado + "s{}".format(c)+":ref -> s{}:ref0 [arrowhead=vee, tailclip=false, arrowtail = vee,dir = both];".format(c+1)+"\n"
			else:
				resultado = resultado + "s{}".format(usuarios.size-1)+":ref -> s0:ref0 [arrowhead=vee, tailclip=false,arrowtail = vee,dir = both];" + "\n"
			aux = aux.next
			c+=1
		resultado = resultado +"}"
		grafos = pydot.graph_from_dot_data(resultado)
		(g,)=grafos
		g.write_jpg('users.jpg')
		os.system('users.jpg')
	def stack_report(self,stack):
		resultado = self.stack_header+"\n"+"score [label=\"{ |"
		aux = stack.head
		while(aux is not None):
			resultado = resultado + aux.content.snake_body()
			if(aux.next is not None):
				resultado = resultado + " | "
			aux = aux.next
		resultado = resultado + "}\"]"+"\n"+"}"
		"""f= open("true_stack.dot","w+")
		f.write(resultado)
		f.close()   
		os.system("dot -Tjpg resultado.dot -o true_stack.jpg")
		os.system('true_stack.jpg')
		"""
		grafos = pydot.graph_from_dot_data(resultado)
		(g,)=grafos
		g.write_jpg('stack.jpg')
		os.system('stack.jpg')
	def snake_report(self,snake):
		resultado =  self.header+"\n"+"n1[label = \"null\"]"+"\n"
		resultado =  resultado + "n2[label = \"null\"]"+"\n"
		aux = snake.head
		c=0
		while(aux is not None):
			resultado = resultado + aux.snake_node(c) +"\n"
			if(aux.next is not None):
				resultado = resultado + "s{}".format(c)+":ref -> s{}".format(c+1)+":ref0 [arrowhead=vee, dir=both, tailclip=false, arrowtail = vee];"+"\n"
			else:
				resultado = resultado + "s{}".format(int(snake.size-1))+":ref -> n2      [arrowhead=vee, tailclip=false,arrowtail = vee];"+"\n"
				resultado = resultado + "s0:ref0 -> n1      [arrowhead=vee, tailclip=false,arrowtail = vee];"+"\n"
			c+=1
			aux = aux.next
		resultado = resultado+"}"
		grafos = pydot.graph_from_dot_data(resultado)
		(g,)=grafos
		g.write_jpg('snake.jpg')
		os.system('snake.jpg')
#algo = Report("/home/renato/Desktop/python/snake/")
"""serpiente = Lista()
serpiente.agregar(Lista(2,4))
serpiente.agregar(Lista(3,4))
serpiente.agregar(Lista(5,10))
serpiente.agregar(Lista(11,5))
algo.snake_report(serpiente)
algo.stack_report(serpiente)
algo.scoreBoard_report(serpiente)
usuarios = Lista()
usuarios.agregar("Renato")
usuarios.agregar("Javi")
usuarios.agregar("Alex")
usuarios.agregar("Jorge")
usuarios.agregar("Hector")
algo.users_report(usuarios)"""
