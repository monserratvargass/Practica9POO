from Personaje import *

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
