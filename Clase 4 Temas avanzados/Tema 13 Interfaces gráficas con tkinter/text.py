#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *

root = Tk()

texto=Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas",12), padx=15, pady=15, selectbackground="red")
#abajo del todo
root.mainloop()