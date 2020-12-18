'''
-----------------------------
 EJERCICIO N°1
 Tu primera GUI
-----------------------------
'''
from tkinter import *

# 1. Creación de una ventana
ventana = Tk()
ventana.title("Curso de Programación")
ventana.geometry("750x200")

# 2. Crear un widget de texto
etiq = Label(ventana, text = "¡Hola mundo!", font=("Times New Roman",30),
                                                       bg = "purple",
                                                        fg = "light green")
etiq.grid(column = 0, row = 0)

# 5. Entrada de datos
texto = Entry(ventana, font=("Times New Roman",20), width = 20,
              state = "disabled")   # 7
texto.grid(column = 2, row = 0)

# 4. Manejar el evento "click del botón"
def clickear():
    entrada = "Bienvenid@, " + texto.get()
    etiq.configure(text = entrada)

# 3. Crear un widget de botón
boton = Button(ventana, text = "Clickéame",font=("Times New Roman",20),
               bg = "orange", fg = "blue",
               command = clickear)
boton.grid(column = 1, row = 0)

# 1. Llama infinitamente a la ventana
texto.focus() # 6
ventana.mainloop()


