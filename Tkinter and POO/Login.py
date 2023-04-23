from tkinter import messagebox

class Login:

    def __init__(self):
        self.__correoE= "panconleche"
        self.__contraE= "monse1601"


    def validar(self,correousuario,contra):
        if (contra ==""  and correousuario==""):
            messagebox.showwarning("Alerta","Los campos deben ser llenados")
        else:
            if(self.__correoE==correousuario and self.__contraE==contra):
                messagebox.showinfo("Exito","Bienvenido(a)")
            else:
                messagebox.showerror("Error","Los datos son incorrectos")
