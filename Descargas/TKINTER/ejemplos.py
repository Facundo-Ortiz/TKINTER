# WIDGETS SON.

#• Label: muestra texto o imágenes.
#• Button: ejecuta una acción.
#• Entry: entrada de texto.
#• Text: texto multilínea.
#• Frame: contenedor para agrupar widgets.

import tkinter as tk

ventana= tk.Tk() # variable que es la ventana

etiqueta = tk.Label(ventana, text='Hello world!') # variable que donde quiero que este el texto

etiqueta.pack() # lo ordena de manera de bloques

ventana.mainloop() # lo mantiene abierto constantemente

def saludar():
    saludo = tk.Label(ventana, text='')
    saludo.config(text=f'Hola nombre Saludo')
    ventana.mainloop() 
    saludo.pack()

boton= tk.Button(ventana, text='Saludar', command=saludar,bg="green")
boton.pack()
