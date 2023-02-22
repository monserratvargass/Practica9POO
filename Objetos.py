from Personaje import *
#Solicitamos
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

#Creamos una instancia de la clase personaje, en este caso la instancia se llama heroe.
Heroe=Personaje()

#Usamos los atributos
print("El personaje se llama"+ Heroe.nombre)
print("Pertenece a la especie"+ Heroe.especie)
print("Y una altura de:"+str(Heroe.altura))

#Usar los metodos
Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(37)
