from tkinter import Tk,Button,Frame,messagebox,Label,ttk, StringVar,Entry
class Login:

    def __init__(self,correousuario ,contraseña):
        self.__correoE= "panconleche"
        self.__contraE= "monse1601"


    def validar(self,correousuario,contra):
        if (contra ==self.__contraE  and correousuario==self.__correoE):
            messagebox.showinfo("Informacion","Bienvenido")
        else:
            messagebox.showerror("Error","Revisa tus datos")
