#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *
root=Tk()
root.title("Hola barry")
root.iconbitmap("hola.ico")
root.resizable(1,1)


frame=Frame(root, width="480", height="320")
#frame.pack(side="bottom", anchor="w")#por defecto ancla el frame o widget en el cento arriba, lo modificamos
frame.pack(fill="both", expand=1)
frame.config(bg="lightgreen")
frame.config(cursor="pirate")
frame.config(bd=25)
frame.config(relief="sunken")


root.config(bg="green")
root.config(cursor="arrow")
root.config(bd=25)
root.config(relief="ridge")
#abajo del todo
root.mainloop()