from tkinter import Tk,Button,Frame

#1.Generar una ventana
ventana=Tk()
ventana.title("Ejemplo de tres Frames")
ventana.geometry("600x400")

#2.Generar secciones/frames dentro de la ventana
seccion1=Frame(ventana,bg="purple")
seccion1.pack(expand=True,fill='both')

seccion2=Frame(ventana,bg="blue")
seccion2.pack(expand=True,fill='both')

seccion3=Frame(ventana,bg="pink")
seccion3.pack(expand=True,fill='both')

#3.Agregamos botones
botonrosa=Button(seccion1,text="Boton Rosa",fg="pink")
botonrosa.place(x=60,y=60,width=100,height=30)

botonnegro=Button(seccion2,text="Boton Negro",fg="black")
botonnegro.grid(row=0,column=0)

botonamarillo=Button(seccion2,text="Boton Amarillo",fg="yellow")
botonamarillo.grid(row=1,column=2)

botonverde=Button(seccion3,text="Boton Verde",fg="green")
botonverde.pack()

#Metodo main para la ejecucion de la ventana
ventana.mainloop() #Siempre al final de la interfaz