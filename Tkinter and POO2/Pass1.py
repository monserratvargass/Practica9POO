from tkinter import messagebox

class Pass1:
    def __init__(self):
        self.__contraseña=8

    def validarcontraseña(self, contra):
        if contra>8:
            self.__contraseña=contra
        else:
            self.__contraseña
