#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *

root = Tk()

#variable dinámica

texto=StringVar()
texto.set("nuevo texto")

frame=Frame(root, width="480",height="320")
frame.pack()

label=Label(frame,text="Hola Barry")#le pasamos el lugar donde queremos que lo muestre -> nuestro frame
label.place(x=0,y=0)#si usamos pack() no respetará el tamaño de nuestro marco y loreiniciará
label.config(bg="green", fg="yellow", font=("Algerian",24))
label.config(textvariable=texto)
#si no vamos a usar el widget label en una variable podemos usarla asi

Label(root, text="una línea mas").pack(anchor="e")#anclado en la raiz y no en frame
Label(root, text="línea2").pack(anchor="nw")

#agregaremos una imágen a una label 
imagen=PhotoImage(file="imagen.gif")
Label(root,image=imagen, bd=0).pack(side="left")
#abajo del todo
root.mainloop()