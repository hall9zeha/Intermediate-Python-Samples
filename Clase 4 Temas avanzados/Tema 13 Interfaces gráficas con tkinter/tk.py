#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *
root=Tk()
root.title("Hola barry")
root.iconbitmap("hola.ico")
root.resizable(0,1)
#abajo del todo
root.mainloop()
