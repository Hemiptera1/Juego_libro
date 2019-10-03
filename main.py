import random
import textwrap

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
		revela_chozas(choza, linea_punteada)
		entrar_a_la_choza(choza, índice)
		combate(pelea, medidor_salud)
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

def revela_chozas(choza, linea_punteada):
	print(linea_punteada)
	print("A continuación se revelarán los ocupantes de las chozas:")
	print(f"Choza 1:{choza[0]} Choza 2:{choza[1]} Choza 3:{choza[2]} Choza 4:{choza[3]} Choza 5:{choza[4]}")
	print(linea_punteada, end = "\n\n")

def entrar_a_la_choza(choza, índice):
	if choza[índice-1] == "Desocupado":
		print("La choza estaba vacía y has sido capaz de hacer uso de ella\nRepones tus fuerzas, has ganado!!")
	elif choza[índice-1] == "Amigo":
		print("Has hallado buenos amigos que te ayudan a reponer tus fuerzas, has ganado!!")
	else:
		print("En guardia!! Te has topado con un enemigo.")
		return pelea = "si"

def atacar(medidor_salud):
	objetivos = ["Player", "Orco"]
	unidad_a_dañar = random.choice(objetivos)
	puntos_vida = medidor_salud[unidad_a_dañar]
	daño = random.randint(10, 15)
	medidor_salud[unidad_a_dañar] = max(puntos_vida - daño, 0)
	if unidad_a_dañar == "Player":
		print("El orco asesta un golpazo con su maza!")
		print(f"Inflingiendo {daño} de daño a sir Ramza")
	elif unidad_a_dañar == "Orco":
		print("Ramza cabalga raudo y lanza un valiente ataque.")
		print(f"Su hoja se hunde en la carne del orco inflingiendo {daño}.")

def combate(pelea, medidor_salud):
	while pelea == "si":
		pelea = input("El enemigo se alza desafiante con {0[Orco]} de vida, lo atacas? (si/no): ".format(medidor_salud))
		if pelea == "no":
				print("Huyes del combate con {0[Player]} de salud".format(medidor_salud))
				break

		atacar(medidor_salud)

		if medidor_salud["Player"] == 0:
			print("Te han asestado un golpe mortal! Has muerto.")
		elif medidor salud["Orco"] == 0:
			print("Luego del ataque tomas distancia y observas a tu enemigo"
				  "Por un momento parece inmovil, pero algo llama tu atención"
				  "Se ladea lentamente hasta desplomarse con un sonoro golpe"
				  "Estaba muerto antes de tocar el suelo", width = 72)


if __name__ == "__main__":
	corre_juego()