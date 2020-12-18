'''
-----------------------------
 EJERCICIO N°3
 Archivos
-----------------------------
'''
from tkinter import *
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk

from os import path

ventana = Tk()
ventana.title("Curso de Programación")
ventana.geometry("750x400")

# 1. Adicionar un diálogo para archivos (elegir archivo y directorio)
#archivo = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),
#                                                  ("all files","*.*")))
#archivos = filedialog.askopenfilename()
#dir = filedialog.askdirectory()
#file = filedialog.askopenfilename(initialdir = path.dirname(__file__))

# 2. Agregar un menú
menu = Menu(ventana)
#menu.add_command(label='Archivo')

nuevo_item = Menu(menu, tearoff = 0)

nuevo_item.add_command(label = "Nuevo")     # Añadir command = clickear()
nuevo_item.add_separator()
nuevo_item.add_command(label = "Editar")

menu.add_cascade(label = "Archivo", menu = nuevo_item)

ventana.config(menu = menu)

# 3. Agregar un Notebook (control de pestañas)
tab_control = ttk.Notebook(ventana)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Primera")
tab_control.pack(expand = 1, fill = 'both')

ventana.mainloop()
