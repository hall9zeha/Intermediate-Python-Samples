#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *
def select():
	cadena=""
	if(leche.get()):
		cadena +="Con leche"
	else:
		cadena+="Sin leche"
	if(azucar.get()):
		cadena +=" y  con azúcar"
	else:
		cadena +=" y sin azúcar"
	if(leche.get()==0 and azucar.get()==0):
		cadena=""

	label.config(text=cadena)

root=Tk()
root.title("Cafetería")
root.config(bd=25)

leche=IntVar()
azucar=IntVar()

imagen=PhotoImage(file="imagen.gif")
Label(root,image=imagen).pack(side="left")


frame=Frame(root)
frame.pack(side="right")
Label(frame,text="¿Cómo quieres el café?").pack()
Checkbutton(frame,text="Con leche", variable=leche, onvalue=1, offvalue=0, command=select).pack(anchor="w")
Checkbutton(frame,text="Con azúcar",variable=azucar,onvalue=1,offvalue=0, command=select).pack(anchor="w")

label=Label(frame)
label.pack()

#abajo del todo
root.mainloop()