class Ancestro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

def construir_arbol(niveles):
    raiz = Ancestro("Ancestro Común")
    ancestros_actuales = [raiz]

    for nivel in range(niveles):
        nuevos_ancestros = []
        for ancestro in ancestros_actuales:
            num_hijos = int(input(f"Cuántos hijos tiene {ancestro.nombre} en el nivel {nivel + 1}? "))
            for i in range(num_hijos):
                nombre_hijo = input(f"Nombre del hijo {i + 1}: ")
                hijo = Ancestro(nombre_hijo)
                ancestro.hijos.append(hijo)
                nuevos_ancestros.append(hijo)
        ancestros_actuales = nuevos_ancestros

    return raiz

def encontrar_ancestro_comun(ancestro, nombre1, nombre2):
    if not ancestro:
        return None

    if ancestro.nombre == nombre1 or ancestro.nombre == nombre2:
        return ancestro

    ancestros_encontrados = []
    for hijo in ancestro.hijos:
        ancestro_encontrado = encontrar_ancestro_comun(hijo, nombre1, nombre2)
        if ancestro_encontrado:
            ancestros_encontrados.append(ancestro_encontrado)

    if len(ancestros_encontrados) == 2:
        return ancestro
    elif len(ancestros_encontrados) == 1:
        return ancestros_encontrados[0]
    else:
        return None

niveles = int(input("Ingrese cuántos niveles de ancestros desea crear: "))
arbol_genealogico = construir_arbol(niveles)

nombre1 = input("Ingrese el primer nombre para comparar ancestros: ")
nombre2 = input("Ingrese el segundo nombre para comparar ancestros: ")

ancestro_comun = encontrar_ancestro_comun(arbol_genealogico, nombre1, nombre2)

if ancestro_comun:
    print(f"El ancestro común más antiguo entre {nombre1} y {nombre2} es {ancestro_comun.nombre}")
else:
    print(f"No se encontró un ancestro común entre {nombre1} y {nombre2}")

