from lista import Lista
from juego import play
from juego import show
usr = None
mensaje = "Snake Menu"+"\n"+"Ingrese el numero de la accion que desea realizar:"
usuarios = Lista()
seleccion = -100
def userSelection(entrada):
	try: 
		seleccion = int(entrada)
		if(seleccion == 0):
			print("Insert your name:")
			name = raw_input()
			usuarios.agregar(name)
			usr = name
			print("User: "+name+" Has been created successfully.")
			return
		usuario = usuarios.getElement(seleccion-1)
		if(usuario is None):
			print("The selected user does not exist.")
			return
		usr = usuario
		print("User: "+usr+" selected successfully.")
	except:
		print("An error has occurred.")
print("Practica 1 EDD.")
print(mensaje)
def options():
	print("0.Play")
	print("1.Scoreboard")
	print("2.User Selection")
	print("3.Reports")
	print("4.Bulk Loading")
	print("5.Salir")
options()
while seleccion!=5:
	if(seleccion != -100):
		options()
	input = raw_input()
	try:
  		seleccion = int(input)
  		if(seleccion == 0):
  			pausa = play(1)
  			if(pausa):
  				print("En pausa.")
  			else:
  				print("juego acabado.")
  		elif (seleccion==1):
  			print("Scoreboard:")
  			#show(players)
  		elif (seleccion==2):
  			print("User Selection:")
  			print("Please, enter the number of the User you'd like to select.")
  			usuarios.imprimir(True)
  			print("If you'd like to create a new user, you can do so by typing 0 instead.")
  			sub_aux = raw_input()
  			userSelection(sub_aux)
  		elif (seleccion==3):
  			print("Reports:")
		elif(seleccion==4):
			print("Bulk Loading.")
			print("Please, type the directory of the file you'd like to bulk load:")
			directory = raw_input()
			print("Users were successfully loaded.")
	except:
  		print("Ocurrio un error. Vuelva a intentar.")
print("Ejecucion terminada con exito.")
