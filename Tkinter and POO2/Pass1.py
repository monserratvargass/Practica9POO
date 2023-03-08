from tkinter import messagebox

class Pass1:
    def __init__(self,contra):
        self.__contraseña=contra

    def validarcontraseña(contra):
        if not 8 >= len(contra):
            return False
        
        numeros=0
        mayusculas=0
        minusculas=0

        for caracteres in contra:
            if caracteres.isspace():
                messagebox.showerror("NO PERMITE CONTRASEÑAS CON ESPACIO")
                return False
            elif caracteres.isdigit():
                messagebox.showinfo("Contiene al menos 4 numeros")
                numeros +=1
            elif caracteres.isupper():
                messagebox.showinfo("Contiene al menos una mayuscula")
                mayusculas +=1
            elif caracteres.islower("Contiene al menos una minuscula"):
                minusculas +=1

        return numeros>4 and mayusculas !=0 and minusculas >=4

    def getEspecie(self):
        return self.__contraseña
    
    def setEspecie(self,contra):
        self.__contraseña= contra