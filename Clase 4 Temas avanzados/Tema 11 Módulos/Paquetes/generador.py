import math
import random

def leer_numeros(ini, fin, mensaje):

	
	while True:
		try:
			valor=int(input(mensaje))
		except:
			print("número no válido")
		else:
			if valor>= ini and valor <=fin:
				break
	return valor

def generador():
	numeros=leer_numeros(1,20,"¿Cuantos números quieres generar? [1 - 20]")
	modo=leer_numeros(1,3 ,"¿Como quieres redondear los números?, 1.- Al alza, 2.- A la baja 3.-Normal")
	listaRandom=[]
	
	
	

	for i in range(numeros):
		numero=random.uniform(0,101)
		listaRandom.append(numero)
		if modo==1:
			print("{}=>{}".format(numero,math.ceil(numero)))
		elif modo==2:
			print("{}=>{}".format(numero,math.floor(numero)))
		elif modo==3:
			print("{}=>{}".format(numero,numero))
	print("")
	print ("lista de números redondeados \n")
	for i in listaRandom:

		print(round(i))
generador()