#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *
def crear_label():

	text=StringVar()
	text.set("Hola barry")
	label=Label(root)
	label.pack()
	label.config(textvariable=text)
#creamos una función para sumar
def suma():
	r.set(float(n1.get()) + float(n2.get()))
	limpiar()
def resta():
	r.set(float(n1.get()) - float(n2.get()))
	limpiar()
def producto():
	r.set(float(n1.get()) * float(n2.get()))
	limpiar()
def limpiar():
	n1.set("")
	n2.set("")

root = Tk()
root.config(bd=10)
n1=StringVar()
n2=StringVar()
r=StringVar()

Label(root,text="Primer número").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root,text="Segundo número").pack()
Entry(root,justify="center",textvariable=n2).pack()
Label(root,text="").pack()
Label(root,text="Resultado").pack()
Entry(root,justify="center",textvariable=r,state="disabled").pack()
Button(root,text="Sumar",command=suma).pack(side="left")
Button(root,text="Restar",command=resta).pack(side="left")
Button(root,text="Multiplicar",command=producto).pack(side="left")



#abajo del todo
root.mainloop()