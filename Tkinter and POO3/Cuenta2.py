from tkinter import messagebox

class cajero:

    def __init__(self):
        self.__nocuenta= 565
        self.__titular= "monserrat vargas"
        self.__edad= 21
        self.__saldo= 8.56

    def consultar(self):
        if(self.__nocuenta==565):
            messagebox.showinfo("La cuenta tiene un saldo de:"+self.__saldo)
        else:
            messagebox.showwarning("La cuenta es inexistente.")

    def ingresar(self):
        if(self.__nocuenta==565):
            messagebox.askyesno("¿Desea ingresar dinero a esta cuenta:")
