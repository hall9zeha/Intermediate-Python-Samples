#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *
def seleccionar():
	monitor.config(text="{}".format(opcion.get()))

def reiniciar():
	opcion.set(None)
	monitor.config(text="")
root=Tk()

opcion=IntVar()

Radiobutton(root,text="opción 1",variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root,text="opcion 2",variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root,text="opcion 3",variable=opcion, value=3, command=seleccionar).pack()

monitor=Label(root)
monitor.pack()

Button(root,text="reiniciar", command=reiniciar).pack()
#abajo del todo
root.mainloop()