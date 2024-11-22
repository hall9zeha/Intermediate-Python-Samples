from io import open

fichero=open("personas.txt","r")

personas=[]
lista=fichero.readlines()
fichero.close()
for linea in lista:
	linea.replace("\n","")
	campo=linea.split(";")
	persona={"id":campo[0],"nombre":campo[1],"apellido":campo[2],"nacimiento":campo[3]}
	personas.append(persona)
for p in personas:
	print("id={} {} {} => {}".format(p["id"],p["nombre"],p["apellido"],p["nacimiento"]))