from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
#*Importar
from ControladorBD import *
#1-Import tkinter module, ttk submodule and the showinfo from tkinter.messagebox
from tkinter.messagebox import showinfo

#*Crear instancia: puente entre los dos archivos
controlador= controladorBD()

#*Metodo que usa mi objeto controlador para insertar
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCo.get(),varPass.get())

#*Metodo que usa mi objeto controlador para buscar un usuario
def ejecutaSelectU():
    rsUsu=controlador.consultarUsuario(varBus.get())
    #Todo se guarda como una cadena, viendo posiciones de cada elemento
    #Iteramos el contenido de la consulta y lo guardamos en CADENA
    for usu in rsUsu:
        cadena= str(usu[0])+" "+usu[1]+" "+usu[2]+" "+str(usu[3])

        textBus.config(state='normal')
        textBus.delete(2.0,'end')
        textBus.insert('end',cadena+'\n')
        textBus.config(state='disabled')

    if(rsUsu):
        print(cadena)
    else:
        messagebox.showinfo('No encontrado','El usuario no exite en base de datos')

#Metodo que usa mi objeto contrlador para consultar usuarios
def ejecutaConsultarU():
      RSUSU=controlador.importarUsuario()
      datosc=tabla.get_children() #Para que se borren los datos ya consultados

      for datoc in datosc:
          tabla.delete(datoc)
    
      for USU in RSUSU:
          cadenacon=str(USU[0])+" "+USU[1]+" "+USU[2]+" "+str(USU[3])

          tabla.insert('',tk.END, values=cadenacon)

          #textCon.config(state='normal')
          #textCon.delete(2.0,'end')
          #textCon.insert('end',cadena+'\n')
          #textCon.config(state='disabled')

          tabla.bind('<<TreeviewSelect>>', ejecutaConsultarU)

def ejecutaModificarU():
    #Avisar al usuario despues de modificar un registro.
    #controlador.actualizarUsuario(varNom1.get(),varCo1.get(),varPass1.get())
    datosm=tabla.get_children() #Para que se borren los datos ya consultados

    for datom in datosm:
        tabla.delete(datom)

    MODUSU=controlador.actualizarUsuario(varAct.get(),varNom1.get(),varCo1.get(),varPass1.get())
    #Ciclo for, cadena de actualizacion, mandar llamar las variables que serian los campos que se van actualizar con su respectiva posicion
    for modificar in MODUSU:
        updatecadena=str(modificar[0])+" "+modificar[1]+" "+modificar[2]+" "+str(modificar[3])

        tabla.update('',tk.END, values=updatecadena)

        varNom1.set(tabla.item('',"values")[1])
        varCo1.set(tabla.item('',"values")[2])
        varPass1.set(tabla.item(' ',"values")[3])

        tabla.bind('<<TreeviewSelect>>', ejecutaModificarU)

    messagebox.showinfo('Confirmacion','El registro se ha modificado')
    
    '''if(MODUSU):
        controlador.actualizarUsuario(varNom1.get(),varCo1.get(),varPass1.get())

        messagebox.showinfo('Confirmacion','El registro se ha modificado')
    else:
        messagebox.showwarning('Error','El registro no se ha modificado')'''

def ejecutaEliminarU():
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

            tabla.bind('<<TreeviewSelect>>', ejecutaEliminarU)

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

#*Command
btnGuardar=Button(pestana1,text='Guardar usuario',command=ejecutaInsert).pack()

#Pestaña 2: Buscar usuario

titulo2=Label(pestana2,text="Buscar usuario",fg="green",font=("Modern",18)).pack()

varBus=tk.StringVar()
lblid=Label(pestana2,text="Identificador de usuario:").pack()
txtid=Entry(pestana2,textvariable=varBus).pack()
btnBusqueda=Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()

subBus=Label(pestana2,text="Registrado:",fg="blue",font=("Modern",15)).pack()
textBus=tk.Text(pestana2,height=5,width=52)
textBus.pack()

#Pestaña 3: Consultar todos los usuarios

titulo3=Label(pestana3,text="Consulta de usuario:",fg="pink",font=("Modern",18)).pack()

btnConsulta=Button(pestana3,text="Buscar",command=ejecutaConsultarU).pack()

subCon=Label(pestana3,text="Todos los registrados",fg="blue",font=("Modern",15)).pack()
textCon=tk.Text(pestana3,height=10,width=104)
textCon.pack()

#2-Define identifiers for columns
columnas=('ID','nombre','correo','contra')
#3-Create a Tkinter´s Treeview widget
tabla=ttk.Treeview(textCon,columns=columnas,show='headings')
#5-Specify the headings for the columns
tabla.heading('ID',text='ID')
tabla.heading('nombre',text='NOMBRE')
tabla.heading('correo',text='CORREO')
tabla.heading('contra',text='CONTRASEÑA')

tabla.pack()

#Pestaña 4: Actualizar
titulo3=Label(pestana4,text="Actualizar usuario",fg="green",font=("Modern",18)).pack()

varAct=tk.StringVar()
lbact=Label(pestana4,text="Identificador de usuario:").pack()
txtact=Entry(pestana4,textvariable=varAct).pack()
#btnActualizar=Button(pestana4,text="Actualizar",command=ejecutaModificarU).pack()

#Ingreso nuevo para actualizar
varNom1=tk.StringVar()
lblNom1=Label(pestana4,text="Nombre: ").pack()
txtNom1=Entry(pestana4,textvariable=varNom1).pack()

varCo1=tk.StringVar()
lblCo1=Label(pestana4,text="Correo: ").pack()
txtCo1=Entry(pestana4,textvariable=varCo1).pack()

varPass1=tk.StringVar()
lblPass1=Label(pestana4,text="Contraseña: ").pack()
txtPass1=Entry(pestana4,textvariable=varPass1).pack()

btnActualizar=Button(pestana4,text="Actualizar",command=ejecutaModificarU).pack()

#Pestaña 5:Eliminar
titulo5=Label(pestana5,text="Eliminar usuario",fg="green",font=("Modern",18)).pack()

varElim=tk.StringVar()
lblElim=Label(pestana5,text="Identificador de usuario:").pack()
txtElim=Entry(pestana5,textvariable=varElim).pack()

btnEliminar=Button(pestana5,text="Eliminar",command=ejecutaEliminarU).pack()

panel.add(pestana1, text="Formulario de usuarios")
panel.add(pestana2, text="Buscar usuarios")
panel.add(pestana3, text="Consultar usuarios")
panel.add(pestana4, text="Actualizar usuarios")

ventana.mainloop()