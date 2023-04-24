from tkinter import Tk,Label,Entry,Button
import tkinter as tk
from Cuenta2 import *

'''def consultar():
    intcajero.consultarsaldo()

def ingresar():
    intcajero.ingresarefectivo()

def retirar():
    intcajero.retirarefectivo()

def depositar():
    intcajero.depositaracuenta()'''

'''def menu():
    #while(True):
        #txtop=float(input('Ingresa la opcion a ejecutar:'))

    if(txtop==1):
        intcajero.consultarsaldo()
    elif(txtop==2):
        intcajero.ingresarefectivo()
    elif(txtop==3):
        intcajero.retirarefectivo()
    elif(txtop==4):
        intcajero.depositaracuenta()

opcion=tk.StringVar()
lblop=Label(ventana,text="Ingresa el numero de eleccion:")
lblop.pack()
txtop=Entry(ventana, textvariable=opcion)
txtop.pack()'''

ventana=Tk()
ventana.title("Cajero automatico")
ventana.geometry("600x400")

con_saldo=tk.StringVar()
lblcon_saldo=Label(ventana,text="Cuenta de la que desea consultar saldo:")
lblcon_saldo.pack()
txtcon_saldo=Entry(ventana, textvariable=con_saldo)
txtcon_saldo.pack()

ing_efectivo=tk.StringVar()
lbling_efectivo=Label(ventana,text="¿Cuanto efectivo desea ingresar?")
lbling_efectivo.pack()
txting_efectivo=Entry(ventana, textvariable=ing_efectivo)
txting_efectivo.pack()

ret_efectivo=tk.StringVar()
lblret_efectivo=Label(ventana,text="¿Cuanto efectivo desea retirar?")
lblret_efectivo.pack()
txtret_efectivo=Entry(ventana, textvariable=ret_efectivo)
txtret_efectivo.pack()

deposito_cuenta=tk.StringVar()
lbldeposito_cuenta=Label(ventana,text="Cuenta a depositar:")
lbldeposito_cuenta.pack()
txtdeposito_cuenta=Entry(ventana, textvariable=deposito_cuenta)
txtdeposito_cuenta.pack()

'''botonMenu=Button(ventana,text="Ejecutar",command=menu)
botonMenu.pack()'''

saldo=0

intcajero=cajero(no_cuenta='121040294',edad="21",saldo=0,titular='Monserrat')

botonConsultar=Button(ventana,text="Consultar saldo",command=intcajero.consultarsaldo)
botonConsultar.pack()

botonIngresar=Button(ventana,text="Ingresar efectivo",command=intcajero.ingresarefectivo)
botonIngresar.pack()

botonRetirar=Button(ventana,text="Retirar efectivo",command=intcajero.retirarefectivo)
botonRetirar.pack()

intcajero=cajero(no_cuenta='121070497',edad="21",saldo=0,titular='Itzel')

botonDepositarCuenta=Button(ventana,text="Depositar a cuenta",command=intcajero.depositaracuenta)
botonDepositarCuenta.pack()

ventana.mainloop()