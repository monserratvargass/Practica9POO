from tkinter import messagebox

class Login:

    def __init__(self,correousuario,contraseña):
        self.__correoE= correousuario
        self.__contraE= contraseña


    def validar(self,correousuario,contraseña):
        correousuario= 'panconleche'
        contraseña= 'Monse1601'

        '''if (contraseña ==""  and correousuario==""):
            messagebox.showwarning("Alerta","Los campos deben ser llenados")
        else:'''
        if(self.__correoE==correousuario and self.__contraE==contraseña):
            messagebox.showinfo("Exito","Bienvenido(a)")
        else:
            messagebox.showerror("Error","Los datos son incorrectos")
