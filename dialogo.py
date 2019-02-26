import random

def frase_aleatoria():
	aleatorio = random.randint(1,17)
	if aleatorio == 1: return "Lo que mas me gusta de " + jugador_aleatorio() + " es que " + afirmacion_positiva_aleatoria()
	if aleatorio == 2: return "Creo que " + jugador_aleatorio() + " " + afirmacion_aleatoria()
	if aleatorio == 3: return "Un dia mi tio me dijo que " + jugador_aleatorio() + " " + afirmacion_negativa_aleatoria() + ", pero sin embargo piensa que " + jugador_aleatorio() + " " + afirmacion_positiva_aleatoria() + " ¿Qué pensáis?"
	if aleatorio == 4: return "Antes del partido de hoy pensaba que " + jugador_aleatorio() + " " + afirmacion_aleatoria() + ". Nunca más."
	if aleatorio == 5: return "La verdad es que " + jugador_aleatorio() + " " + afirmacion_aleatoria()
	if aleatorio == 6: return "No me gusta nada que " + jugador_aleatorio() + " piense así. Hacen falta más como " + jugador_aleatorio() + " y menos tontería." 
	if aleatorio == 7: return "Me parece que " + jugador_aleatorio() + " " + afirmacion_aleatoria()
	if aleatorio == 8: return "Ultimamente me parece que " + jugador_aleatorio() + " " + afirmacion_aleatoria()
	if aleatorio == 9: return "En esta temporada " + jugador_aleatorio() + " " + afirmacion_aleatoria() + ". Sin embargo " + jugador_aleatorio() + " " + afirmacion_positiva_aleatoria()
	if aleatorio == 10: return "A veces me da la impresión de que " + jugador_aleatorio() + " " + afirmacion_aleatoria() + ". Espero que no sea solo yo..."
	if aleatorio == 11: return "Si nos hubiesemos dado cuenta antes de que " + jugador_aleatorio() + " " + afirmacion_aleatoria() + " no habríamos llegado a esta situación."
	if aleatorio == 12: return jugador_aleatorio() + " no da su mejor nivel internacionalmente. Es un jugador mediocre, no como " + jugador_aleatorio()
	if aleatorio == 13: return jugador_aleatorio() + " " + afirmacion_aleatoria() + ", no como " + jugador_aleatorio()
	if aleatorio == 14: return jugador_aleatorio() + " " + afirmacion_aleatoria() + " la verdad..."
	if aleatorio == 15: return "Se esperaba más de " + jugador_aleatorio()
	if aleatorio == 16: return "Lo de " + jugador_aleatorio() + " estaba merecido."
	if aleatorio == 17: return jugador_aleatorio() + ", " + jugador_aleatorio() + " y " + jugador_aleatorio() + "."

def jugador_aleatorio():
	aleatorio = random.randint(1,25)
	if aleatorio == 1: return "Keylor Navas"
	if aleatorio == 2: return "Casilla"
	if aleatorio == 3: return "Courtois"
	if aleatorio == 4: return "Luca"
	if aleatorio == 5: return "Vallejo"
	if aleatorio == 6: return "Sergio Ramos"
	if aleatorio == 7: return "Varane"
	if aleatorio == 8: return "Nacho"
	if aleatorio == 9: return "Marcelo"
	if aleatorio == 10: return "Odriozola"
	if aleatorio == 11: return "Reguilón"
	if aleatorio == 12: return "Kroos"
	if aleatorio == 13: return "Modric"
	if aleatorio == 14: return "Casemiro"
	if aleatorio == 15: return "Valverde"
	if aleatorio == 16: return "Llorente"
	if aleatorio == 17: return "Asensio"
	if aleatorio == 18: return "Brahim"
	if aleatorio == 19: return "Isco"
	if aleatorio == 20: return "Ceballos"
	if aleatorio == 21: return "Mariano"
	if aleatorio == 22: return "Benzema"
	if aleatorio == 23: return "Bale"
	if aleatorio == 24: return "Lucas Vázquez"
	if aleatorio == 25: return "Vinicius"

def afirmacion_aleatoria():
	aleatorio = random.randint(1,25)
	if aleatorio == 1: return "está en su mejor momento"
	if aleatorio == 2: return "podría hacer más"
	if aleatorio == 3: return "es el mejor que hemos tenido desde hace un tiempo"
	if aleatorio == 4: return "siempre falla los pases"
	if aleatorio == 5: return "gana en el 4-3-3"
	if aleatorio == 6: return "se ha ganado la mala fama que tiene"
	if aleatorio == 7: return "a la hora de la verdad no da lo prometido"
	if aleatorio == 8: return "se despista en el centro del campo"
	if aleatorio == 9: return "no entrena lo suficientemente duro"
	if aleatorio == 10: return "no está a lo que está"
	if aleatorio == 11: return "tiene un sprint muy bueno"
	if aleatorio == 12: return "tiene las horas contadas en el RM"
	if aleatorio == 13: return "es indepe"
	if aleatorio == 14: return "lo tenia merecido"
	if aleatorio == 15: return "no da el nivel para nuestro equipo"
	if aleatorio == 16: return "solo está por el dinero"
	if aleatorio == 17: return "vale su peso en oro"
	if aleatorio == 18: return "mucho lirili y poco lerele"
	if aleatorio == 19: return "la ha pifiado"
	if aleatorio == 20: return "ignora muchas cosas"
	if aleatorio == 21: return "miente"
	if aleatorio == 22: return "va para entrenador"
	if aleatorio == 23: return "se ha cambiado de carril"
	if aleatorio == 24: return "ahora piensa de otra manera"
	if aleatorio == 25: return "no se centra en los partidos importantes"

def afirmacion_positiva_aleatoria():
	aleatorio = random.randint(1,25)
	if aleatorio == 1: return "está en su mejor momento"
	if aleatorio == 2: return "sí que le echa huevos"
	if aleatorio == 3: return "es el mejor que hemos tenido desde hace un tiempo"
	if aleatorio == 4: return "chuta a matar"
	if aleatorio == 5: return "gana en el 4-3-3"
	if aleatorio == 6: return "es muy maduro"
	if aleatorio == 7: return "lo da todo"
	if aleatorio == 8: return "recuerda a Raul"
	if aleatorio == 9: return "está fuerte"
	if aleatorio == 10: return "tiene consistencia en el equipo"
	if aleatorio == 11: return "tiene un sprint muy bueno"
	if aleatorio == 12: return "tiene un saque espectacular"
	if aleatorio == 13: return "no falla una"
	if aleatorio == 14: return "es un jugador de equipo"
	if aleatorio == 15: return "da el nivel de sobra para nuestro equipo"
	if aleatorio == 16: return "se nota que quiere a la aficion"
	if aleatorio == 17: return "vale su peso en oro"
	if aleatorio == 18: return "puede jugar solo"
	if aleatorio == 19: return "tiene valentía"
	if aleatorio == 20: return "es culto, y se le nota"
	if aleatorio == 21: return "dice la verdad"
	if aleatorio == 22: return "va para entrenador"
	if aleatorio == 23: return "se mantiene firme pese a todo"
	if aleatorio == 24: return "ahora piensa de otra manera"
	if aleatorio == 25: return "se centra en los partidos importantes"

def afirmacion_negativa_aleatoria():
	aleatorio = random.randint(1,25)
	if aleatorio == 1: return "no está en su mejor momento"
	if aleatorio == 2: return "podría hacer más"
	if aleatorio == 3: return "es el peor que hemos tenido desde hace un tiempo"
	if aleatorio == 4: return "siempre falla los pases"
	if aleatorio == 5: return "pierde en el 4-3-3"
	if aleatorio == 6: return "se ha ganado la mala fama que tiene"
	if aleatorio == 7: return "a la hora de la verdad no da lo prometido"
	if aleatorio == 8: return "se despista en el centro del campo"
	if aleatorio == 9: return "no entrena lo suficientemente duro"
	if aleatorio == 10: return "no está a lo que está"
	if aleatorio == 11: return "tiene un sprint muy mediocre"
	if aleatorio == 12: return "tiene las horas contadas en el RM"
	if aleatorio == 13: return "es indepe"
	if aleatorio == 14: return "lo tenia merecido"
	if aleatorio == 15: return "no da el nivel para nuestro equipo"
	if aleatorio == 16: return "solo está por el dinero"
	if aleatorio == 17: return "no da lo prometido"
	if aleatorio == 18: return "mucho lirili y poco lerele"
	if aleatorio == 19: return "la ha pifiado"
	if aleatorio == 20: return "ignora muchas cosas"
	if aleatorio == 21: return "miente"
	if aleatorio == 22: return "nos perjudica"
	if aleatorio == 23: return "se ha cambiado de carril"
	if aleatorio == 24: return "ya no es como antes"
	if aleatorio == 25: return "no se centra en los partidos importantes"

def imprime_frases(num =  10):
	while num > 0:
		print(frase_aleatoria())
		num = num-1