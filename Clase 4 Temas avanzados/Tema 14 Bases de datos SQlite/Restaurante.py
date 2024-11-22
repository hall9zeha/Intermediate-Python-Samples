import sqlite3
def crear_db():
	conexion=sqlite3.connect("restaurante.db")

	cursor=conexion.cursor()
	try:

		cursor.execute('''
			create table categoria (
			id integer primary key autoincrement,
			nombre varchar(100) unique not null 

			)
			''')
		cursor.execute('''
			create table plato(
			id integer primary key autoincrement,
			nombre varchar(100) unique not null,
			categoria_id integer not null,
			foreign key(categoria_id) references categoria (id)
			)
			''')
		#cuando se crean las tablas no hace falta crear un commit como cuando insertamos 
		#conexion.commit()
		conexion.close()
	except:
		print("las tablas ya existen")
	else: 
		print("bd y tablas creadas correctamente")

def crear_categoria():
	categoria=input(str("ingrese categoria: "))

	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()
	try:
		cursor.execute("insert into categoria values(null,'{}')".format(categoria))
		conexion.commit()
		conexion.close()
	except sqlite3.IntegrityError:
		print("\nLa categoría {} ya existe".format(categoria))
	else:
		print("categoría {} registrada".format(categoria))
def agregar_plato():
	conexion=sqlite3.connect("restaurante.db")
	cursor=conexion.cursor()
	cursor.execute("select * from categoria")
	categorias=cursor.fetchall()
	print("categorias disponibles")
	for categoria in categorias:
		print(categoria[0], categoria[1] )
	id_categoria=int(input ("\ningrese el id de la categoría: \n"))
	plato=input("ingrese el nombre del plato\n")
	try:
		cursor.execute("insert into plato values(null,'{}',{})".format(plato,id_categoria))
		conexion.commit()
		conexion.close()
	
	except sqlite3.IntegrityError:
		print("el plato {} ya existe".format(plato)) 
	else:
		print("Plato {} agregado  correctamente".format(plato))

def mostrar_menu():
	conexion=sqlite3.connect("restaurante.db")
	cursor = conexion.cursor()
	categorias=cursor.execute("select  * from categoria").fetchall()

	for categoria in categorias:
		print(categoria[1],"\n")
		platos=cursor.execute("select  * from plato where categoria_id={}".format(categoria[0])).fetchall()
		for plato in platos:
			print(plato[1])


#crear la base de datos
crear_db()
#menu de opciones
while True:
	print("\nBienvenido al menu del restaurante\n")
	a = input("\nIngrese una opción:\n[1]agregar categoría\n[2]Agragar plato\n[3]Mostrar menu\n[4]Salir\n")
	if a== "1":
		crear_categoria()
	elif a=="2":
		agregar_plato()
	elif a=="3":
		mostrar_menu()
	elif a=="4":
		print ("Adios baby")
		break
	else:
		print("opción incorrecta")





