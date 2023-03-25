from Login import *

ventana=Tk()
ventana.title("LOGIN")
ventana.geometry("600x400")

correousuario=Label(ventana, text="Ingrese su correo del usuario:")
correousuario.pack()

CorreoUsuario=StringVar()
cu=Entry(ventana, width=40, textvariable=CorreoUsuario)
cu.pack()
correoEntry= cu.get()

contraseña=Label(ventana, text="Ingrese contraseña:") 
contraseña.pack()

contraseña1=StringVar()
co=Entry(ventana,textvariable=contraseña1,show="*")
co.pack()
contraEntry= co.get()


login1=Login(correoEntry,contraEntry)

def ejecutaVal():
    login1.validar(contraseña1.get(),CorreoUsuario.get())

botonValidar=Button(ventana,text="Validar",command=login1.validar)
botonValidar.pack()

ventana.mainloop()