from io import open
import pickle
import sys
class Personaje:

	def __init__(self, nombre, vida ,ataque, defenza,alcance):
		self.nombre=nombre
		self.vida=vida
		self.ataque=ataque
		self.defenza=defenza
		self.alcance=alcance



	def __str__(self):
		return "{} => vida {} ataque {} defenza {} alcance {}".format(self.nombre,self.vida,self.ataque,self.defenza,self.alcance)

class Gestor:

	personajes=[]

	def __init__(self):
		self.cargar()

	def agregar(self, p):

		for i in self.personajes:
			if i.nombre==p.nombre:
				return
		self.personajes.append(p)
		self.guardar()

	def mostrar(self):
		if len(self.personajes)==0:
			print("no hay personajes")
			return
		for p in self.personajes:
			print(p)
	def guardar(self):

		fichero=open('personajes.pckl','wb')
		pickle.dump(self.personajes,fichero)
		fichero.close()
		
	def cargar(self):
		fichero=open('personajes.pckl','ab+')
		fichero.seek(0)

		try:
			
			self.personajes=pickle.load(fichero)
		except:
			pass
			#print("no hay personajes")
		finally:
			fichero.close()
			
			print("se han cargado {} personajes".format(len(self.personajes)))
	def borrar(self, nombre):
		try:
			for i in self.personajes:
				if i.nombre==nombre:
					self.personajes.remove(i)
					print("personaje {} borrado".format(nombre))
					self.guardar()
					return
		except:
			print("ha ocurrido un error")

	

g=Gestor()


#g.agregar(Personaje("caballero",4,2,4,2))
#g.agregar(Personaje("guerrero",2,4,2,4))
#g.agregar(Personaje("arquero",2,4,1,8))
g.mostrar()


