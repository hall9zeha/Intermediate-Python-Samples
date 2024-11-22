import sqlite3

conexion=sqlite3.connect("usuarios_autoincremental.db")
cursor=conexion.cursor()
"""
cursor.execute('''
		create table usuarios (
			Dni varchar(8) primary key,
			Nombres varchar(100),
			edad integer,
			email varchar(100)
		)	''')
"""

"""cursor.execute('''
	create table productos (
	id integer primary key autoincrement,
	nombre varchar(100) not null,
	marca varchar(50)not null,
	precio float nit null

	)
	''')
"""
#productos=[
#('teclado','razer',320),
#('camara','logitech',120)

#]

#cursor.executemany("insert into productos values(null,?,?,?)",productos)

'''
usuarios= [
('11111111','Barry',30,'barry@mail.com'),
('22222222','Martha',32,'martha@mail.com'),
('33333333','Tara',27,'tara@mail.com'),
('44444444','Ella',30,'ella@mail.com')
]
cursor.executemany("insert into usuarios values(?,?,?,?)",usuarios)
'''

"""cursor.execute('''
	create table usuarios(
	id integer primary key autoincrement,
	dni varchar(8) unique,
	nombres varchar(100),
	edad integer,
	email varchar(50)
	)
	''')
"""
usuarios = [
('11111111','Barry',30,'barry@mail.com'),
('22222222','Martha',32,'martha@mail.com'),
('33333333','Lizy',28,'liz@mail.com'),
('44444444','Tara',31,'tr@mail.com')
]

cursor.executemany("insert into usuarios values(null,?,?,?,?)",usuarios)
conexion.commit()
conexion.close()