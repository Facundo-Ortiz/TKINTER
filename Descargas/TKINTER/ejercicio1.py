# Crear una pequeña app con etiqueta de texto 
# que sea un saludo integrando el nombre que ingrese el usuario,
#  entrada para que el usuario ingrese nombre y botón que sea que cuando lo 
# presiones obtenga el nombre y devuelva el saludo completo . 

import tkinter as tk # Tkinter es una libreria, o creador de interfaz grafica

ventana = tk.Tk() # Esta es la variable que sera la VENTANA 
ventana.title('TkApp') # Esto le da el titulo a la VENTANA
ventana.geometry('300x350') # Con este metodo te permite adjustar el tamaño de la VENTANA
ventana.resizable(False,False)
etiqueta = tk.Label(ventana, text= "Ingrese su nombre:")
etiqueta.pack
ingreso_nombre = tk.Entry(ventana)
ingreso_nombre.pack()

def saludar():
    nombre = ingreso_nombre.get() 
saludo = tk.Label(ventana, text='')
saludo.config(text=f'Hola nombre Saludo')
ventana.mainloop() 
saludo.pack()

boton= tk.Button(ventana, text='Saludar', command=saludar,bg="green")
boton.pack()
