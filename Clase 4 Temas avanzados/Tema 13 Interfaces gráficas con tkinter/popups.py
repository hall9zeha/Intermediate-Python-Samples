#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *
from tkinter import messagebox as MessageBox # lo renombramos para usarlo es opcional
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
def popup():

	#MessageBox.showinfo("Hola","Hola Barry")
	#MessageBox.showwarning("Alerta","no eres Barry")
	#MessageBox.showerror("Error","Error Barry")
	#resultado =MessageBox.askquestion("Salir","¿Seguro que quieres salir")
	#if resultado=="yes":
	#	root.destroy()

	#resultado =MessageBox.askokcancel("Salir","¿Seguro que quieres salir")
	#if resultado:
	#	root.destroy()
	#resultado =MessageBox.askyesno("Salir","¿Seguro que quieres salir")
	#if resultado:
	#	root.destroy()
	#resultado =MessageBox.askretrycancel("Reintentar","¿Seguro que quieres reintentar")
	#if resultado:
	#	root.destroy()
	#color=ColorChooser.askcolor(title="Escoge un color")
	#print(color)

	#ruta=FileDialog.askopenfilename(title="Abrir fichero", initialdir="C:",
	#	filetypes=(("fichero de texto","*.txt"),("ficheros avanzados","*.txt2")
	#		,("todos los ficheros","*.*")))

	fichero = FileDialog.asksaveasfile(title="Guradar fichero",mode="r+", defaultextension="txt")
	if fichero is not None:
		fichero.write("Hola barry")
		fichero.close()
	print(fichero)

root=Tk()


Button(root,text="mostrar popup",command=popup).pack()
#abajo del todo
root.mainloop()