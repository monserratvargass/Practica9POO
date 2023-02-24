from Personaje import *
#Solicitamos datos para el objeto
print("")
print("### Solicitud datos heroe ###")
especieH=input("Escribe la especie del heroe:")
nombreH=input("Escribe el nombre del heroe:")
alturaH=float(input("Escribe la altura del heroe:"))
recargaH=int(input("Ingresa las balas para el heroe"))

print("### Solicitud datos villanos ###")
especieV=input("Escribe la especie del villano:")
nombreV=input("Escribe el nombre del villano:")
alturaV=float(input("Escribe la altura del villano:"))
recargaV=int(input("Ingresa las balas para el villano"))

#Creamos los objetos
Heroe=Personaje(especieH,nombreH,alturaH)
Villano=Personaje(especieV,nombreV,alturaV)

Heroe.setNombre("Pepe Pecas")


#Creamos una instancia de la clase personaje, en este caso la instancia se llama heroe.
#Heroe=Personaje()

#Usamos los atributos
#parctica 10: usamos los atributos Heroe y Villano
#complemento, hacemos uso del get
print("")
print("El personaje se llama"+ Heroe.getNombre())
print("Pertenece a la especie"+ Heroe.getEspecie())
print("Y una altura de:"+str(Heroe.getAltura()))
#5.
Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargaH)

print("")
print("El personaje se llama"+ Villano.getNombre())
print("Pertenece a la especie"+ Villano.getEspecie())
print("Y una altura de:"+str(Villano.getAltura()))
#5
Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargaV)
#Villano.__pensar() #no encuentra, pq es atributo privado

#5.Usar los metodos y agregar metodos para el villano

