#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *
from tkinter import messagebox as MessageBox # lo renombramos para usarlo es opcional
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
from io import open
ruta="" #fichero global

def nuevo():
	global ruta#le indicamos que la variable que usaremos dentro del método es la variable global
	mensaje.set("Nuevo fichero")
	ruta=""
	texto.delete(1.0,"end")
	root.title("Editor")

def abrir():
	global ruta
	mensaje.set("Abrir fichero")
	ruta=FileDialog.askopenfilename(initialdir=".",filetype=(("Ficheros de texto","*.txt"),),
		title="Abrir un fichero de texto")
	if ruta !="":
		fichero=open(ruta,"r")
		contenido=fichero.read()
		texto.delete(1.0,"end")
		texto.insert("insert",contenido)
		fichero.close()
		root.title(ruta + "Editor")
	

def guardar():

	mensaje.set("Guardar fichero")
	if ruta !="":
		contenido=texto.get(1.0,"end-1c")
		fichero=open(ruta,"w+")
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Fichero guardado")
	else: 
		guardar_como()
def guardar_como():
	global ruta
	mensaje.set("Guardar fichero como")
	fichero =FileDialog.asksaveasfile(title="Guardar fichero",mode="w", defaultextension="txt")
	if fichero is not None:
		ruta=fichero.name
		contenido=texto.get(1.0, "end-1c")
		fichero=open(ruta,"w+")
		fichero.write(contenido)
		fichero.close()
		mensaje.set("Fichero guardado")
	else:
		mensaje.set("Cancelado")
		ruta=""




root=Tk()
root.title("Editor")

#Menu superior
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)

filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="salir")

menubar.add_cascade(menu=filemenu,label="Archivo")

#caja de texto
texto=Text(root)
texto.pack(fill="both",expand=1)
texto.config(bd=0, padx=6,pady=4,font=("Consolas",12))

#monitor label
mensaje=StringVar()
mensaje.set("Bienvenido Barry")
monitor=Label(root,textvar=mensaje,justify="left")
monitor.pack(side="left")

root.config(menu=menubar)

#abajo del todo
root.mainloop()