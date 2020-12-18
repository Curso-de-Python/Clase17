'''
-----------------------------
 EJERCICIO N°2
 Combobox
-----------------------------
'''
from tkinter import *
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from tkinter.ttk import *
from tkinter.ttk import Progressbar
from tkinter import ttk

# 1. Creación de una ventana
ventana = Tk()
ventana.title("Curso de Programación")
ventana.geometry("750x400")

# 2. Agregar un combobox (menú desplegable)
menu = Combobox(ventana)
menu["values"] = (1,2,3,4,5,"Hola")
menu.current(1) # El 2do item es el predeterminado
menu.grid(column = 0, row = 0)

# 4. Valor predeterminado para el checkbutton
estado_check = BooleanVar()     # Pueden cambiar por IntVar()
estado_check.set(False)

# 3. Agregar un checkbutton (casilla de verificación)
check = Checkbutton(ventana, text = "Elígeme", var = estado_check)
check.grid(column = 0, row = 1)

# 6. Configurar eventos para el radio button
def clickearRadio():
    print("Has seleccionado el número", seleccionado.get())

# 7. Para obtener el valor del radio button
seleccionado = IntVar()

# 5. Agregar radio buttons (casillas de selección)
radio1 = Radiobutton(ventana, text = "Primero", value = 1,
                     variable = seleccionado, command = clickearRadio)
radio2 = Radiobutton(ventana, text = "Segundo", value = 2)
radio3 = Radiobutton(ventana, text = "Tercero", value = 3)
radio1.grid(column = 1, row = 0)
radio2.grid(column = 2, row = 0)
radio3.grid(column = 3, row = 0)

# 8. Agregar un ScrolledText (área de texto)
texto = st.ScrolledText(ventana, width = 40, height = 10)
texto.grid(column = 0, row = 2)
texto.insert(INSERT, "Tu texto va aquí...\nhola\nafss")
#texto.delete(1.0,END)

# 9. Crear un MessageBox (mensaje informativo)
def clickearBoton():
    mb.showinfo('Título del mensaje', 'Contenido del mensaje')
    mb.showwarning('Título de la advertencia', 'Contenido de la advertencia')
    mb.showerror('Título del error', 'Contenido del error')
    rpta = mb.askquestion('Título de la pregunta','Te hago una pregunta')
    rpta = mb.askyesno('Título del pregunta','¿Sí o no?')
    rpta = mb.askyesnocancel('Título del pregunta','¿Sí, no o cancelas?')
    rpta = mb.askokcancel('Título del pregunta','¿Aceptas o cancelas?')
    rpta = mb.askretrycancel('Título del pregunta','¿Quieres volver a intentar?')

boton = Button(ventana, text = "Clickéame", command = clickearBoton)
boton.grid(column = 0, row = 3)

# 10. Agregar un SpinBox (selección de números)
var = IntVar()
var.set(36)
spin = Spinbox(ventana, from_ = 0, to = 100, width = 10,
               textvariable = var) # También con values(3,8,11)
spin.grid(column = 0, row = 4)

# 11. Agregar un Progressbar (Barra de progreso)
estilo = ttk.Style()
estilo.theme_use('default')
estilo.configure('blue.Horizontal.TProgressbar', background='blue')

bar = Progressbar(ventana, length = 200, style = 'blue.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column = 0, row = 5)

# Llama infinitamente a la ventana
ventana.mainloop
