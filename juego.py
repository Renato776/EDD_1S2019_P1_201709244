def play(s):
	o = raw_input()
	if(o=="pausa"):
		#print("Seleccionar pausa")
		return True
	else:
		return False
def show(players):
	aux = players.head
	while aux is not None:
		aux = aux.next
		print(aux.content.name)


	
