#importamos el módulo para las interfaces gráficas
#para ejecutar un fichero con interface gráfica y que no nos muestre la terminal sino solamente la ventana
#le cambiamos el nombre de la extensión a .pyw
from tkinter import *

root = Tk()

#variable dinámica

#Una forma de crear los formularios  poniéndolos en frames distintos para cada línea
"""
#Frame 1
frame1=Frame(root)
frame1.pack()

label1=Label(frame1,text="Nombre")
label1.pack(side="left")

entry1=Entry(frame1)
entry1.pack(side="right")
#************************************
#Frame2
frame2=Frame(root)
frame2.pack()

label2=Label(frame2, text="Apellidos")
label2.pack(side="left")

entry2=Entry(frame2)
entry2.pack(side="right")
"""

#ahora lo haremos con una grilla que es la mejor manera al menos por ahora

label1=Label(root,text="Nombre")
label1.grid(row=0,column=0,sticky="e",padx=5,pady=5)

entry1=Entry(root)
entry1.grid(row=0,column=1,sticky="e",padx=5,pady=5)
entry1.config(justify="right",state="disable")#disable o normal si queremos en el campo entry
label2=Label(root, text="Apellidos")
label2.grid(row=1,column=0,sticky="e",padx=5,pady=5)

entry2=Entry(root)
entry2.grid(row=1,column=1,sticky="e",padx=5,pady=5)
entry2.config(justify="center",show="*")#si es un campo contraseña
#abajo del todo
root.mainloop()