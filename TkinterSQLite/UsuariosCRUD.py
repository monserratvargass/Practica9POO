from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana=Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)

#Definir el contenido de cada una de las pestañas
#Pestaña 1: Formulario de registro
titulo=Label(pestana1,text="Registro usuarios",fg="blue",font=("Modern",18)).pack()

varNom=tk.StringVar()
lblNom=Label(pestana1,text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()

varCo=tk.StringVar()
lblCo=Label(pestana1,text="Correo: ").pack()
txtCo=Entry(pestana1,textvariable=varCo).pack()

varPass=tk.StringVar()
lblPass=Label(pestana1,text="Contraseña: ").pack()
txtPass=Entry(pestana1,textvariable=varPass).pack()

btnGuardar=Button(pestana1,text='Guardar usuario').pack()

panel.add(pestana1, text="Formulario de usuarios")
panel.add(pestana2, text="Buscar usuarios")
panel.add(pestana3, text="Consultar usuarios")
panel.add(pestana4, text="Actualizar usuarios")

ventana.mainloop()