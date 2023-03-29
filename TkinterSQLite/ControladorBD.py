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
    
    def consultarUsuario(self,id):
        #1.Realizar conexion BD
        conx=self.conexionBD()
        #2.Verificar que el id vacio
        if(id==""):
            messagebox.showwarning("Cuidado","Escribe un identificador")
            conx.close()
        else:
            #3.Ejecutar la consulta
            try:
                cursor=conx.cursor()
                sqlSelect="select * from TbRegistrados where id="+id
                #Ejecutamos y cerramos conexion
                cursor.execute(sqlSelect)
                RSusuario=cursor.fetchall() #Toma lo que esta en el cursor, mueve hacia la vista
                conx.close()

                return RSusuario
            except sqlite3.OperationalError:
                print("Error de consulta")
