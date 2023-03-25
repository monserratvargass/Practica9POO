from tkinter import *
from Pass1 import *
import tkinter as tk

#password=Pass1(contr)

#def ejecutaVal():
    #password.validarcontraseña(Pass1.get())

ventana=Tk()
ventana.title("Password")
ventana.geometry("300x150")

password1=Label(ventana, text="Ingrese cantidad de caracteres:")
password1.pack()

#entry_pass1=tk.StringVar()
pa=Entry(ventana, width=40, textvariable=Pass1)
pa.pack()
paEntry= pa.get()

password3=Label(ventana, text="")
password3.pack()

password2=Entry(ventana,width=40,textvariable=Pass1)
password2.pack()


#botonValidar=Button(ventana,text="Validar",command=ejecutaVal())
#botonValidar.pack()

ventana.mainloop()