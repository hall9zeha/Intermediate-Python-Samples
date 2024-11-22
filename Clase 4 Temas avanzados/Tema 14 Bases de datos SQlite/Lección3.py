import sqlite3 

conexion=sqlite3.connect("usuarios_autoincremental.db")
cursor=conexion.cursor()

cursor.execute("update usuarios set nombres ='Barry Zea' where id=1")
cursor.execute("delete from usuarios where id= 1")
cursor.execute("select * from  usuarios where id=1")
usuario=cursor.fetchone()
print (usuario)
conexion.commit()
conexion.close()