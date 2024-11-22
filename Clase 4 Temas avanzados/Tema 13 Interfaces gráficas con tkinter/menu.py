#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *


root=Tk()

menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_separator()
filemenu.add_command(label="Cerrar", command=root.quit)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")
menubar.add_cascade(label="Archivo",menu=filemenu)
menubar.add_cascade(label="Editar",menu=editmenu)
menubar.add_cascade(label="Ayuda",menu=helpmenu)
#abajo del todo
root.mainloop()