from tkinter import messagebox
import string

class Logica:

    def __init__(self,romanos,arabigos):
        self.__romanos= romanos
        self.__arabigos= arabigos

    def convertir_romanos_arabigos(self):
        entrada=string.ascii_uppercase
        if(entrada==self.__romanos):
            messagebox.showinfo('ROMANOS A ARABIGOS', self.__arabigos)
        else:
            messagebox.showerror('Error','El numero romano no es valido')

    def convertir_arabigos_romanos(self):
        entrada1=0
        if(entrada1==self.__arabigos):
            messagebox.showinfo('ARABIGOS A ROMANOS', self.__romanos)
        else:
            messagebox.showerror('Error','El numero arabigo no es valido')