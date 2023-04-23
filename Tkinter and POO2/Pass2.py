from tkinter import *
from Pass1 import *
import random
import string
import tkinter as tk

password=Pass1()

def ejecutaGen():
    txtco.delete(0, tk.END)
    txtco.insert(0, ejecutaGen)

    num=int(longitud.get())
    password.validarcontraseña(num)

    caracteres=string.punctuation
    mayusculas=string.ascii_uppercase
    letras=string.ascii_letters

    contraseña=''

    especiales= messagebox.askyesno('Caracteres especiales','¿Desea usar caracteres especiales en su contraseña?')
    mayus=messagebox.askyesno('Mayusculas','¿Desea usar mayusuclas en su contraseña?')

    if especiales==True and mayus==True:
        alfabeto=caracteres + letras
        for i in range(num):
            contraseña+=''.join(random.choice(alfabeto))
            print(contraseña)
        return contraseña
    if especiales==False and mayus==True:
        alfabeto=letras
        for i in range(num):
            contraseña+=''.join(random.choice(alfabeto))
        return contraseña
    if especiales==True and mayus==False:
        alfabeto=caracteres + mayusculas
        for i in range(num):
            contraseña+''.join(random.choice(alfabeto))
        return contraseña
    if especiales==False and mayus==False:
        alfabeto=mayusculas
        for i in range(num):
            contraseña+=''.join(random.choice(alfabeto))
        return contraseña


ventana=Tk()
ventana.title("Generador de contraseñas")
ventana.geometry("300x150")

longitud=tk.StringVar()
lbllongitud=Label(ventana,text="Indique longitud de la contraseña: ")
lbllongitud.pack()
txtlongitud=Entry(ventana, textvariable=longitud)
txtlongitud.pack()

lblco=Label(ventana,text='Contraseña generada')
lblco.pack()
txtco=Entry(ventana)
txtco.pack()

'''minus=tk.StringVar()
lblminus=Label(ventana,text="Indique numero minimo de minusculas: ")
lblminus.pack()
txtminus=Entry(ventana, textvariable=minus)
txtminus.pack()

mayus=tk.StringVar()
lblmayus=Label(ventana,text="Indique numero minimo de mayus: ")
lblmayus.pack()
txtmayus=Entry(ventana, textvariable=mayus)
txtmayus.pack()

num=tk.StringVar()
lblnum=Label(ventana,text="Indique numero minimo de caracteres numericos: ")
lblnum.pack()
txtnum=Entry(ventana, textvariable=num)
txtnum.pack()'''

botonGenerar=Button(ventana,text="Generar contraseña", command=ejecutaGen)
botonGenerar.pack()

ventana.mainloop()