from tkinter import messagebox
import string
import re

class Logica:

    def __init__(self,romanos,arabigos):
        self.__romanos__= romanos
        self.__arabigos__= arabigos

    '''def convertir_romanos_arabigos(self):
        romanos={'I':1,'II':2,'III':3}
        #entrada=string.ascii_uppercase
        if(romanos==self.__romanos):
            messagebox.showinfo('ROMANOS A ARABIGOS', self.__arabigos)
        else:
            messagebox.showerror('Error','El numero romano no es valido')

    def convertir_arabigos_romanos(self):
        entrada1=0
        if(entrada1==self.__arabigos):
            messagebox.showinfo('ARABIGOS A ROMANOS', self.__romanos)
        else:
            messagebox.showerror('Error','El numero arabigo no es valido')'''
    
    '''def convertir_romanos_arabigos(self, numeroromanos):
        numeroromanos = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50}
        numeroarabicos = 0
        i = 0
        while i < len(numeroromanos):
            if i < len(numeroromanos) - 1 and tuple(numeroromanos[i:i+2]) in list(numeroromanos):
                numeroarabicos += numeroromanos[numeroromanos[i:i+2]]
                i += 2
            else:
                numeroarabicos += numeroromanos[numeroromanos[i]]
                i += 1
        if numeroarabicos < 1 or numeroarabicos > 50:
            raise ValueError("Roman numeral must be between 1 and 50")
        return numeroarabicos
    
    def convertir_arabigos_romanos(self, numeroarabico):
        numromano = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L'}
        numeroromano = ''
        while numeroarabico > 0:
            for arabic, roman in reversed(sorted(numromano.items())):
                while numeroarabico >= arabic:
                    numeroromano += roman
                    numeroarabico -= arabic
        return numeroromano'''
    
    def convertir_romanos_arabigos(self):
        romanos = str(self.__romanos__)
        romanos = romanos.upper()
        romanos = romanos.replace(' ','')
        romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
        arabigos = 0
        
        if romanos=="VX":
            messagebox.showerror("Error","El numero es incorrecto")
        else:
            if re.match("^[IVXLivxl ]*$", romanos):
                for i in range(len(romanos)):
                    if i > 0 and romano[romanos[i]] > romano[romanos[i-1]]:
                        arabigos += romano[romanos[i]] - 2 * romano[romanos[i-1]]
                    else:
                        arabigos += romano[romanos[i]]
                if arabigos < 1 or arabigos > 50:
                    messagebox.showerror("Error", "El número romano debe ser entre I y L")
                    return None
                else:
                    return arabigos
            else:
                messagebox.showerror("Error", "Ingrese numero valido.")
                return None
            
    def convertir_arabigos_romanos(self):
        araB = int(self.__arabigos__)
        if (araB>=1 and araB<=50):
            romanos = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L'}
            romano = ''
            for value, symbol in sorted(romanos.items(), reverse=True):
                while araB >= value:
                    romano += symbol
                    araB -= value
            return romano
        else:
            messagebox.showerror("Error","El numero debe estar entre 1 y 50")
