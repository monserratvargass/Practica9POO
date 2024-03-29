from tkinter import messagebox
import sqlite3

class BDcontrolador:

    def __init__(self):
        pass

    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/monse/Documents/Fundamentos POO/Parcial 2/Practica9POO/Inicio Examen3/BDExportaciones.db")
            print("Conectado a la BD")
            return conexion #Devuelve el valor de la conexion
        except sqlite3.OperationalError:
             print("No se pudo conectar a la BD")

    def guardarPedimento(self,trans,adu):
        #1.Mandar llamar el metodo conexion
        conex=self.conexionBD()

        #2.Validar vacios
        if(trans==""or adu==""):
            messagebox.showwarning("Aguas!!!","Formulario incompleto")
            conex.close()
        else:
            #3.Realizar insert a BD
            #4. Preparamos las variables necesarias
            cursor1=conex.cursor()
            #conH=self.encriptarContra(con)
            datos=(trans,adu)
            sqlInsert="insert into TBPedimentos(Transporte,Aduana) values(?,?)"

            #5.Ejecutamos el Insert
            cursor1.execute(sqlInsert,datos)
            conex.commit()
            conex.close()
            messagebox.showinfo("Exito","Pedimento guardado")

    def consultarPedimento(self,aduana):
        #1.Realizar conexion BD
        conx=self.conexionBD()
        #2.Verificar que el id vacio
        if(aduana==""):
            messagebox.showwarning("Cuidado","Escribe aduana")
            conx.close()
        else:
            #3.Ejecutar la consulta
            try:
                cursor2=conx.cursor()
                sqlSelect="select * from TBPedimentos where Aduana="+aduana
                #Ejecutamos y cerramos conexion
                cursor2.execute(sqlSelect)
                RSusuario=cursor2.fetchall() #Toma lo que esta en el cursor, mueve hacia la vista
                conx.close()

                return RSusuario
            except sqlite3.OperationalError:
                print("Error de consulta")

    def eliminarPedimento(self,id):
         #1.Realizar conexion BD
        conx=self.conexionBD()
        #2.Verificar que el id vacio
        if(id==""):
            messagebox.showwarning("Cuidado","Escribe un identificador")
            conx.close()
        else:
            #3.Ejecutar lo de eliminar
            try:
                cursor3=conx.cursor()
                sqlEliminar="delete from TBPedimentos where IDExpo="+id #Se eliminaran los registros a partir del id seleccionado
                #Ejecutamos y cerramos conexion
                cursor3.execute(sqlEliminar)
                Elmusuario=cursor3.fetchall() #Toma lo que esta en el cursor, mueve hacia la vista
                conx.commit()
                conx.close()

                return Elmusuario
            except sqlite3.OperationalError:
                print("No se puede ejecutar la funcion eliminar")
