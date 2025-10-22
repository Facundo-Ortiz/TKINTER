import tkinter as tk

ventana= tk.Tk()

frame1= tk.Frame(ventana, bg='Pink', width=120, height= 120)
frame1.pack()

ventana.title('Inicio de Sesion')

ventana.geometry('300x350')

ventana.resizable(False,False)

user= tk.Label(ventana, text='usuario')

user.pack()

ent_user= tk.Entry(ventana)

ent_user.pack()

contra= tk.Label(ventana, text='Contraseña')

contra.pack()

ent_contra= tk.Entry(ventana)

ent_contra.pack()

usuario= "admin"
contrasena= "python123"

def inicio():
    entrada = ent_user.get()
    contrasen= ent_contra.get()
    if ent_user==usuario and ent_contra==contrasena:
       mensaje_bienvenido.config(text= 'Bienvenido')
    else:
        mensaje_error.config(text= 'hubo un error. intente de nuevo.')
        
    
boton= tk.Button(ventana, text="Verificar", command= inicio)
boton.pack()

mensaje_bienvenido= tk.Label(ventana)
mensaje_error= tk.Label(ventana)
mensaje_bienvenido.pack()
mensaje_error.pack()
ventana.mainloop()