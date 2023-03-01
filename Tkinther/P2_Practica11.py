from tkinter import Tk,Button,Frame,messagebox

#5.Agregar funcion de mensaje
def mostrarmensaje():
    messagebox.showinfo("Informacion","Te informo que todo fallo con exito")
    messagebox.showerror("Error","Perdon te falle")
    print(messagebox.askokcancel("Pregunta","Seguro que quieres guardar algo?"))
    print(messagebox.askquestion("Pregunta","Seguro quieres guradar algo?"))
    print(messagebox.askretrycancel("Pregunta","Seguro quieres guardar algo?"))
    print(messagebox.askyesno("Pregunta","Seguro quieres guardar?"))
    print(messagebox.askyesnocancel("Pregunta","Seguro quieres guardar"))

#6.Funcion agregar botones
def agregarboton():
    botonverde.config(text="+",bg="green",fg="white")
    botonNuevo=Button(seccion3,text="Boton nuevo")
    botonNuevo.pack()

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
botonrosa=Button(seccion1,text="Boton Rosa",fg="pink",command=mostrarmensaje)
botonrosa.place(x=60,y=60,width=100,height=30)

botonnegro=Button(seccion2,text="Boton Negro",fg="black")
botonnegro.grid(row=0,column=0)

botonamarillo=Button(seccion2,text="Boton Amarillo",fg="#a5b2ff")
botonamarillo.grid(row=1,column=2)

botonverde=Button(seccion3,text="Boton Verde",fg="green",command=agregarboton)
botonverde.pack()

#4. Revisar los posicionamientos

#Metodo main para la ejecucion de la ventana
ventana.mainloop() #Siempre al final de la interfaz