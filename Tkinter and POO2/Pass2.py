from tkinter import *
from Pass1 import *
import tkinter as tk

password=Pass1()

def ejecutaVal():
    password.validarcontraseña(Pass1.get())

ventana=Tk()
ventana.title("Password")
ventana.geometry("300x150")

password1=Label(ventana, text="Ingrese su correo del usuario:")
password1.pack()

entry_pass1=tk.StringVar()
pa=Entry(ventana, width=40, textvariable=Pass1, validate="key",validatecommand=entry_pass1)
pa.pack()
paEntry= pa.get()

def limitador(entry_pass1):
    if len(entry_pass1.get())>0:
        entry_pass1.set(entry_pass1.get()[:8])



botonValidar=Button(ventana,text="Validar",command=ejecutaVal())
botonValidar.pack()

ventana.mainloop()