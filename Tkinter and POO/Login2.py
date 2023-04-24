from tkinter import *
from Login import *
import tkinter as tk

login1=Login(correousuario='panconleche',contraseña='Monse1601')

def ejecutaVal():
    login1.validar(CorreoUsuario.get(),contraseña1.get())

ventana=Tk()
ventana.title("LOGIN")
ventana.geometry("600x400")

seccion1=Frame(ventana)
seccion1.pack(expand=True,fill='both')

titulo=Label(seccion1,text="Login",bg="black",fg="white",font=("Helvetica",18))
titulo.pack()

CorreoUsuario=tk.StringVar()
lblcu=Label(seccion1,text="Ingrese correo: ")
lblcu.pack()
txtcu=Entry(seccion1, textvariable=CorreoUsuario,takefocus=True)
txtcu.pack()

contraseña1=tk.StringVar()
lblco=Label(seccion1,text="Ingrese contraseña: ")
lblco.pack()
txtco=Entry(seccion1,show="*",textvariable=contraseña1)
txtco.pack()

botonValidar=Button(ventana,text="Validar",command=ejecutaVal)
botonValidar.pack()

ventana.mainloop()