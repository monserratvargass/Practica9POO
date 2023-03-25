from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:

    def __init__(self):
        pass

    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/monse/Documents/Fundamentos_POO/Parcial_2/Practica9POO/TkinterSQLite/DatabaseUsuarios.db")
            print("Conectado a la BD")
            return conexion #Devuelve el valor de la conexion
        except sqlite3.OperationalError:
             print("No se pudo conectar a la BD")

    def guardarUsuario(self,nom,cor,con):
        #1.Mandar llamar el metodo conexion
        conx=self.conexionBD()

        #2.Validar vacios
        if(nom==""or cor=="" or con==""):
            messagebox.showwarning("Aguas!!!","Formulario incompleto")
            conx.close()
        else:
            #3.Realizar insert a BD
            #4. Preparamos las variables necesarias
            cursor= conx.cursor()
            datos=(nom,cor,con)
            sqlInsertar="insert into TbRegistrados(nombre,correo,contra) values(?,?,?)"

            #5.Ejecutamos el Insert
            cursor.execute(sqlInsertar,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario guardado")

    '''def encriptarContra(self,con):

        conPlana=con
        conPlana= conPlana.encode() #Convertir a bytes
        sal= bcrypt.gensalt()

        conHa=bcrypt.hashpw(conPlana,sal)
        print(conHa)

        #Regresamos la contraseña encriptada
        return conHa'''
