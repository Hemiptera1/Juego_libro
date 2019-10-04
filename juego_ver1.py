import random
import textwrap

def marco_embellecedor(mensaje):
	marco = "-" * 72
	print(marco)
	print(mensaje)
	print(marco, end="\n\n")

def corre_juego():
	seguir_jugando = "si"
	ancho = 72
	linea_punteada = "-" * ancho
	medidor_salud = {"Jugador": 40, "Orco": 35}
	
	presentando(linea_punteada, ancho)
	misión(linea_punteada)

	while seguir_jugando == "si":
		choza = chozas()
		índice = elección_de_usuario()
		revela_chozas(choza, índice)
		pelea = entrar_a_la_choza(choza, índice)
		combate(medidor_salud, pelea)
		seguir_jugando = input("Deseas seguir jugando? (si/no): ")

def presentando(linea_punteada, ancho):
	print(linea_punteada)
	print("El ataque de los orcos!!")
	print(linea_punteada)
	mensaje = (
        "The war between humans and their arch enemies, Orcs, was in the "
        "offing. Sir Foo, one of the brave knights guarding the southern "
        "plains began a long journey towards the east through an unknown "
        "dense forest. On his way, he spotted a small isolated settlement."
        " Tired and hoping to replenish his food stock, he decided to take"
        " a detour. As he approached the village, he saw five huts. There "
        "was no one to be seen around. Hesitantly, he  decided to enter..")
	print(textwrap.fill(mensaje, width = ancho))
	print(linea_punteada, end = "\n\n")

def misión(linea_punteada):
	print(linea_punteada)
	print("Misión: Debes elegir con cuidado la tienda en la que ingresará sir Ramza.")
	print("Ten cuidado, pues podrías encontrarte con un enemigo")
	print(linea_punteada, end = "\n\n")

def chozas():
	choza = list()
	posibilidad = ["Enemigo", "Amigo", "Desocupado"]
	while len(choza) < 5:
		elección_cpu = random.choice(posibilidad)
		choza.append(elección_cpu)
	return choza

def elección_de_usuario():
	índice = int(input("Escoge la tienda en la que se adentrará sir Ramza (1-5): "))
	return índice

def revela_chozas(choza, índice):
	mensaje = f'''A continuación se revelarán los ocupantes de las chozas:
Choza 1:{choza[0]} Choza 2:{choza[1]} Choza 3:{choza[2]} Choza 4:{choza[3]} Choza 5:{choza[4]}
Entras en la choza número {str(índice)}:'''
	marco_embellecedor(mensaje)

def entrar_a_la_choza(choza, índice):
	pelea = "no"
	if choza[índice-1] == "Desocupado":
		print("La choza estaba vacía y has sido capaz de hacer uso de ella para reponer tus fuerzas, has ganado!!")
	elif choza[índice-1] == "Amigo":
		print("Has hallado buenos amigos que te ayudan a reponer tus fuerzas, has ganado!!")
	elif choza[índice-1] == "Enemigo":
		print("En guardia!! Te has topado con un enemigo.")
		pelea = "si"
	return pelea

def atacar(medidor_salud):
	objetivos = ["Jugador", "Orco"]
	unidad_a_dañar = random.choice(objetivos)
	puntos_vida = medidor_salud[unidad_a_dañar]
	daño = random.randint(10, 15)
	medidor_salud[unidad_a_dañar] = max(puntos_vida - daño, 0)
	if unidad_a_dañar == "Jugador":
		mensaje = f'''El orco asesta un golpazo con su maza inflingiendo {daño} de daño a sir Ramza'''
		print(mensaje)
	elif unidad_a_dañar == "Orco":
		mensaje = f'''Ramza cabalga raudo y lanza un golpe que se hunde en la carne del orco inflingiendo {daño} puntos de daño.'''
		print(mensaje)

def combate(medidor_salud, pelea):
	while pelea == "si":
		pelea = input("El enemigo se alza desafiante con {0[Orco]} de vida, tus fuerzas: {0[Jugador]}, atacas? (si/no): ".format(medidor_salud))
		if pelea == "no":
				print("Huyes del combate con {0[Jugador]} de salud".format(medidor_salud))
				break
		elif pelea == "si":
			atacar(medidor_salud)

		if medidor_salud["Jugador"] == 0:
			print("Te han asestado un golpe mortal! Has muerto.")
			break
		elif medidor_salud["Orco"] == 0:
			mensaje = '''Luego de propinar semejante golpe te apartas de tu enemigo y lo observas
Por un momento permanece inmovil, luego comienza a ladearse lentamente hasta desplomarse sobre el suelo
Estaba muerto antes de tocar el suelo'''
			break


if __name__ == "__main__":
	corre_juego()