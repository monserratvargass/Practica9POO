from tkinter import messagebox

class cajero:

    def __init__(self):
        self.nocuenta= 48521662
        self.titular= 'Monserrat'
        self.edad= 22
        self.saldo= 1000

    def consultarsaldo(self):
        return self.saldo
        '''if(self.__n):
            messagebox.showinfo("La cuenta tiene un saldo de:"+self.__saldo)
        else:
            messagebox.showwarning("La cuenta es inexistente.")'''

    def ingresarefectivo(self,monto):
        self.saldo+=monto
    

    def retirarefectivo(self,monto):
        if(self.saldo>=monto):
            self.saldo-=monto
            return True
        else:
            return False
            #messagebox.askyesno("¿Desea ingresar dinero a esta cuenta:")

    def depositaracuenta(self,cuentanueva,monto):
        if self.saldo>=monto:
            self.saldo-=monto
            cuentanueva.saldo+=monto
            return True
        else:
            return False