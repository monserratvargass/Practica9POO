from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:

    def __init__(self):
        pass

    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/monse/Documents/Fundamentos POO/Parcial 2/Practica9POO/TkinterSQLite/DatabaseUsuarios.db")
            print("Conectado a la BD")
            return conexion #Devuelve el valor de la conexion
        except sqlite3.OperationalError:
             print("No se pudo conectar a la BD")

    def guardarUsuario(self,nom,cor,con):
        #1.Mandar llamar el metodo conexion
        conex=self.conexionBD()

        #2.Validar vacios
        if(nom==""or cor=="" or con==""):
            messagebox.showwarning("Aguas!!!","Formulario incompleto")
            conex.close()
        else:
            #3.Realizar insert a BD
            #4. Preparamos las variables necesarias
            cursor=conex.cursor()
            conH=self.encriptarContra(con)
            datos=(nom,cor,con)
            sqlInsert="insert into TbRegistrados(nombre,correo,contra) values(?,?,?)"

            #5.Ejecutamos el Insert
            cursor.execute(sqlInsert,datos)
            conex.commit()
            conex.close()
            messagebox.showinfo("Exito","Usuario guardado")
            
    #Para encriptar:
    def encriptarContra(self,con):
        conPlana=con
        conPlana= conPlana.encode() #Convertir a bytes
        sal= bcrypt.gensalt()
        #Encriptamos
        conHa=bcrypt.hashpw(conPlana,sal)
        print(conHa)

        #Regresamos la contraseña encriptada
        return conHa
