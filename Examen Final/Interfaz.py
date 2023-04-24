from tkinter import *
from Logica import *
from tkinter import ttk
import tkinter as tk

romanos=['I','II','III']
arabigos=['1,2,3']

conversor=Logica(romanos,arabigos)

#conversor=Logica()

def ra():
    arabigos={'1,2,3'}
    #romanos={'I':1,'II':2,'III':3}
    if(romanos==txtromanos.get()):
        conversor.convertir_romanos_arabigos(romanos)
    else:
        messagebox.showinfo('Convertidor',str(arabigos))

def ar():
    romanos={'I':1,'II':2,'III':3}
    #arabigos={'1,2,3'}
    if(arabigos==txtarabigo.get()):
        conversor.convertir_arabigos_romanos(arabigos)
    else:
        messagebox.showinfo('Convertidor',romanos)


ventana=Tk()
ventana.title("LOGIN")
ventana.geometry("600x400")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)

romanos=tk.StringVar()
lblromanos=Label(pestana1,text="Numero romano a convertir:")
lblromanos.pack()
txtromanos=Entry(pestana1, textvariable=romanos)
txtromanos.pack()

arabigo=tk.StringVar()
lblarabigo=Label(pestana2,text="Numero arabigo a convertir:")
lblarabigo.pack()
txtarabigo=Entry(pestana2, textvariable=arabigo)
txtarabigo.pack()

botonConvertirRA=Button(pestana1,text="Convertir",command=ra)
botonConvertirRA.pack()

botonConvertirAR=Button(pestana2,text="Convertir",command=ar)
botonConvertirAR.pack()

panel.add(pestana1, text="Conversor de romanos a arabigo")
panel.add(pestana2, text="Conversor de arabigo a romano")

ventana.mainloop()