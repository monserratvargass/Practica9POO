from tkinter import messagebox, simpledialog

class cajero:

    def __init__(self,no_cuenta,titular,edad,saldo):
        self.__nocuenta= no_cuenta
        self.__titular= titular
        self.__edad= edad
        self.__saldo= saldo

    def consultarsaldo(self):
        no_cuenta='121040294'
        titular= 'Monserrat'
        edad="21"
        saldo= 1200
        if(self.__nocuenta==no_cuenta and self.__titular==titular):
            self.__saldo=saldo
            messagebox.showinfo("Consulta de saldo","Su saldo es de:"+str(self.__saldo))
        else:
            messagebox.showerror("Error","Los datos no coinciden")
        #return self.__saldo
        '''if(self.__n):
            messagebox.showinfo("La cuenta tiene un saldo de:"+self.__saldo)
        else:
            messagebox.showwarning("La cuenta es inexistente.")'''

    def ingresarefectivo(self):
        no_cuenta='121040294'
        titular= 'Monserrat'
        edad="21"
        saldo= 1200
        if(self.__nocuenta==no_cuenta and self.__titular==titular):
            ask=simpledialog.askfloat(title="a depositar",prompt="¿Cuanto desea depositar?")
            self.__saldo=saldo+ask
            messagebox.showinfo('Consulta de saldo','Su saldo actual es de:'+str(self.__saldo))
        else:
            messagebox.showerror("Error","Los datos no coinciden")

    
    def retirarefectivo(self):
        no_cuenta='121040294'
        titular= 'Monserrat'
        edad="21"
        saldo= 1200
        if(self.__nocuenta==no_cuenta and self.__titular==titular):
            ask=simpledialog.askfloat(title="a retirar",prompt="¿Cuanto desea retirar?")
            self.__saldo=saldo-ask
            messagebox.showinfo('Consulta de saldo','Su saldo actual es de:'+str(self.__saldo))
        else:
            messagebox.showerror("Error","Los datos no coinciden")

        
    def depositaracuenta(self):
        no_cuenta='121070497'
        titular= 'Itzel'
        edad="21"
        saldo= 100
        if(self.__nocuenta==no_cuenta and self.__titular==titular):
            ask=simpledialog.askfloat(title="a depositar",prompt="¿Cuanto desea depositar?")
            self.__saldo=saldo+ask
            messagebox.showinfo('Consulta de saldo','Su saldo actual es de:'+str(self.__saldo))
        else:
            messagebox.showerror("Error","Los datos no coinciden")