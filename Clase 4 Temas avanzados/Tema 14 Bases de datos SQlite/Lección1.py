import sqlite3

conexion=sqlite3.connect("dbEjemplo.db")

cursor=conexion.cursor()
#cursor.execute("CREATE TABLE usuarios (nombre varchar(100),edad integer, email varchar(100))")
#cursor.execute("INSERT INTO usuarios values('Martha',32,'matha@mail.com')")

#cursor.execute("select * from usuarios")
#usuario=cursor.fetchone()

#insertando de forma masiva 
"""
usuarios=[
('Barry',30,'barry@ejemplo.com'),
	('Tara',27,'tara@ejemplo.com'),
	('Beatriz',30,'bea@ejemplo.com')
]
cursor.executemany("insert into usuarios values(?,?,?)",usuarios)

"""

#recuperando datos de forma masiva

cursor.execute("select * from usuarios")
usuarios=cursor.fetchall()

for usuario in usuarios:
	print("Nombre: ", usuario[0], "- Email: ",usuario[2])

#print(usuario)
conexion.commit()
conexion.close()