import sys
#recibiremos una linea desde la terminal y la repetiremos cuantas veces pongamos 
if len(sys.argv)==3:
	texto=sys.argv[1] #1 porque esta lista que nos muestra el sistema la posición 0 es el nombre del script
	num=int(sys.argv[2])
	for r in range(num):
		print(texto)
else:
	print("Error introduce los parámetros correctos")
	print("Ejemplo", 'texto entre comillas', 5)
#Al guardar el archivo siempre guardar con codificacion UTF-8 para evitar errores en ejecución por caracteres en español y tildes



