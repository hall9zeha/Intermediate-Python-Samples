from io import open


inc=int(input("ingrese 1 para incrementar o 0 para decrementar: "))


fichero=open("contador.txt","a+")
fichero.seek(0)
c=fichero.readline()

if len(c)==0:
	c="0"
	fichero.seek(0)
	fichero.write(c)
fichero.close()

try:
	contador=int(c)
	if inc==1:
		contador +=1
	elif inc==0:
		contador -=1
	print(contador)

	#escribimos el fichero

	fichero=open("contador.txt","w")
	
	fichero.write(str(contador))
	fichero.close()
except:
	print("error")
			




