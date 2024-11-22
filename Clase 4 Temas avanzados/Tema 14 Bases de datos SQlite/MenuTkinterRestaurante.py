from tkinter import *
import sqlite3

root=Tk()
root.title("Bar restaurante Zeha's - Menu")
root.resizable(0,0)
root.config(bd=25,relief="sunken")

Label(root, text="   Bar Zeha's  ", fg="darkgreen", font=("Times New Roman",28,"bold italic")).pack()
Label(root, text="   Menú del día  ", fg="green", font=("Times New Roman",24,"bold italic")).pack()

Label(root, text=" ").pack()
conexion=sqlite3.connect("restaurante.db")
cursor=conexion.cursor()
categorias=cursor.execute("select * from categoria").fetchall()
for categoria in categorias:
		Label(root,text=categoria[1],fg="black", font=("Times New Roman",20,"bold italic")).pack()
		print("\n")
		platos=cursor.execute("select  * from plato where categoria_id={}".format(categoria[0])).fetchall()
		for plato in platos:
			Label(root,text=plato[1],fg="gray", font=("Times New Roman",14,"italic")).pack()
		Label(root, text=" ").pack()
conexion.close()

Label(root,text="S/. 320  Total", fg="green", font=("Times New Roman",20,"bold")).pack(side="right")
root.mainloop()