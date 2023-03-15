from tkinter import messagebox

class examen:

    def __init__(self,nom,apP,apM,nac,carr):
        self.__nombre= nom
        self.__apellidoP= apP
        self.__apellidoM= apM
        self.__nacimiento= nac
        self.__carrera= carr

    def generar(self):
            messagebox.showinfo("23"+self.getNacimiento[:2]+self.getNombre[:1]+self.getApellidoP[:1]+
                                self.getApellidoM[:1]+"895"+self.getCarrera[:3])
   
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre= nom
    
    def getApellidoP(self):
        return self.__apellidoP
    
    def setApellidoP(self,apP):
        self.__apellidoP= apP

    def getApellidoM(self):
        return self.__apellidoM
    
    def setApellidoM(self,apM):
        self.__apellidoM= apM

    def getNacimiento(self):
        return self.__nacimiento
    
    def setApellidoM(self,nac):
        self.__nacimiento= nac

    def getCarrera(self):
        return self.__carrera
    
    def setApellidoM(self,carr):
        self.__carrera= carr
