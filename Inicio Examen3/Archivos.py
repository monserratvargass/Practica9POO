from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
#*Importar
from BDControlador import *

#*Crear instancia: puente entre los dos archivos
controlador= BDcontrolador()

#*Metodo que usa mi objeto controlador para insertar
def ejecutaInsert():
    controlador.guardarPedimento(varTransporte.get(),varAduana.get())

#*Metodo que usa mi objeto controlador para buscar un usuario
def ejecutaSelectP():
    rsUsu=controlador.consultarPedimento(varPedAdu.get())
    #Todo se guarda como una cadena, viendo posiciones de cada elemento
    #Iteramos el contenido de la consulta y lo guardamos en CADENA
    for usu in rsUsu:
        cadena= str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])

        textPED.config(state='normal')
        textPED.delete(2.0,'end')
        textPED.insert('end',cadena+'\n')
        textPED.config(state='disabled')

    if(rsUsu):
        print(cadena)
    else:
        messagebox.showinfo('No encontrado','El pedimento no existe en base de datos')

def ejecutaEliminarP():
    #Solicitar una confirmacion antes de Eliminar
        #DELUSU=controlador.eliminarUsuario(varElim.get())
    datose=tabla.get_children()

    for datoe in datose:
        tabla.delete(datoe)

        #for delete in DELUSU:
            #deletecadena=str(delete[0])+" "+delete[1]+" "+delete[2]+" "+str(delete[3])
    #pregunta
    ask=messagebox.askyesno('Pregunta','¿Estas seguro de eliminar el usuario?')
    #Condiciones para verdadero el registro es eliminado de lo contrario no se elimina
    if ask==True:
        DELUSU=controlador.eliminarUsuario(varElim.get())
        for delete in DELUSU:
            deletecadena=str(delete[0])+" "+delete[1]+" "+delete[2]+" "+str(delete[3])

            tabla.delete('',tk.END, values=deletecadena)

            tabla.bind('<<TreeviewSelect>>', ejecutaEliminarP)

        messagebox.showinfo('Confirmacion','Su registro seleccionado ha sido eliminado')

    else:
        messagebox.showerror('Error','Su registro seleccionado no ha sido eliminado')

ventana=Tk()
ventana.title("CRUD de usuarios")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)
pestana5=ttk.Frame(panel)

#Definir el contenido de cada una de las pestañas
#Pestaña 1: Formulario de registro
titulo=Label(pestana1,text="Registros de pedimentos",fg="blue",font=("Modern",18)).pack()

varTransporte=tk.StringVar()
lblTransporte=Label(pestana1,text="Transporte: ").pack()
txtTransporte=Entry(pestana1,textvariable=varTransporte).pack()

varAduana=tk.StringVar()
lblAduana=Label(pestana1,text="Aduana: ").pack()
txtAduana=Entry(pestana1,textvariable=varAduana).pack()


#*Command
btnGuardar=Button(pestana1,text='Guardar pedimento',command=ejecutaInsert).pack()

#Pestaña 2: Consultar por aduana

titulo2=Label(pestana2,text="Buscar pedimento",fg="green",font=("Modern",18)).pack()

varPedAdu=tk.StringVar()
lblid=Label(pestana2,text="Aduana:").pack()
txtid=Entry(pestana2,textvariable=varPedAdu).pack()
btnBusqueda=Button(pestana2,text="Buscar",command=ejecutaSelectP).pack()

subPED=Label(pestana2,text="Registrado:",fg="blue",font=("Modern",15)).pack()
textPED=tk.Text(pestana2,height=5,width=52)
textPED.pack()

#2-Define identifiers for columns
columnas=('IDExpo','Transporte','Aduana')
#3-Create a Tkinter´s Treeview widget
tabla=ttk.Treeview(textPED,columns=columnas,show='headings')
#5-Specify the headings for the columns
tabla.heading('IDExpo',text='IDEXPO')
tabla.heading('Transporte',text='TRANSPORTE')
tabla.heading('Aduana',text='ADUANA')

tabla.pack()


#Pestaña 5:Eliminar
titulo5=Label(pestana5,text="Eliminar pedimento",fg="green",font=("Modern",18)).pack()

varElim=tk.StringVar()
lblElim=Label(pestana5,text="Identificador de pedimento:").pack()
txtElim=Entry(pestana5,textvariable=varElim).pack()

btnEliminar=Button(pestana5,text="Eliminar",command=ejecutaEliminarP).pack()

panel.add(pestana1, text="REGISTROS DE INCIOS DE PEDIMENTOS")
panel.add(pestana2, text="BUSQUEDA DE PEDIMENTOS POR ADUANAS")
#Nueva pestaña para eliminar usuarios
panel.add(pestana5, text="ELIMINAR PEDIMENTOS")

ventana.mainloop()