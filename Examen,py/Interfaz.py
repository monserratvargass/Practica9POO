from tkinter import Tk,Label,Entry

ventana=Tk()
ventana.title("Examen, solicitud de datos")
ventana.geometry("600x400")

nombre=Label(ventana,text="Ingrese el nombre:")
nombre.pack()
nom=Entry(ventana, width=40, textvariable=nombre)
nom.pack()

apellidoP=Label(ventana,text="Ingrese el apellido paterno:")
apellidoP.pack()
apP=Entry(ventana, width=40, textvariable=apellidoP)
apP.pack()

apellidoM=Label(ventana,text="Ingrese el apellido materno:")
apellidoM.pack()
apM=Entry(ventana, width=40, textvariable=apellidoM)
apM.pack()

nacimiento=Label(ventana,text="Ingrese año de nacimiento:")
nacimiento.pack()
nac=Entry(ventana, width=40, textvariable=nacimiento)
nac.pack()

carrera=Label(ventana,text="Ingrese carrera a la que pertenece")
carrera.pack()
carr=Entry(ventana, width=40, textvariable=carrera)
carr.pack()

ventana.mainloop()
