class Ancestro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

# Crear el árbol genealógico con niveles predefinidos
def crear_arbol_predefinido():
    raiz = Ancestro("xavier")
    nivel_1A = Ancestro("emilioI")
    nivel_1B = Ancestro("xavierII")
    nivel_2A = Ancestro("harry")
    nivel_2B = Ancestro("juan,")
    nivel_2C = Ancestro("pablo")
    nivel_2D = Ancestro("alan")
    nivel_3A = Ancestro("carlos")
    nivel_3B = Ancestro("patricio")
    nivel_3C = Ancestro("carla")
    nivel_3D = Ancestro("carlota")
    nivel_3E = Ancestro("domingo")
    nivel_3F = Ancestro("atanasio")
    nivel_3G = Ancestro("jorge")
    nivel_3H = Ancestro("rodrigo")
    nivel_4A = Ancestro("carlosII")
    nivel_4A = Ancestro("carmen")
    nivel_4A = Ancestro("gepeto")
    nivel_4A = Ancestro("victor")
    nivel_4A = Ancestro("guadalupe")
    nivel_4A = Ancestro("petra")
    nivel_4A = Ancestro("adrian")
    nivel_4A = Ancestro("cesar")
    nivel_4A = Ancestro("helena")
    nivel_5B = Ancestro("carlosIII,karol,carola,lucero,andres,fernando,ricardo,misael,claudia")
    nivel_6A = Ancestro("larry,kevin,santiago,britany")

    nivel_1.hijos.append(nivel_2A)
    nivel_1.hijos.append(nivel_2B)
    nivel_2A.hijos.append(nivel_3A)
    nivel_2B.hijos.append(nivel_3B)
    raiz.hijos.append(nivel_1)

    return raiz

# Encontrar el ancestro común
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

# Crear el árbol genealógico predefinido
arbol_genealogico = crear_arbol_predefinido()

# Solicitar nombres para comparar
nombre1 = input("Ingrese el primer nombre para comparar ancestros: ")
nombre2 = input("Ingrese el segundo nombre para comparar ancestros: ")

ancestro_comun = encontrar_ancestro_comun(arbol_genealogico, nombre1, nombre2)

if ancestro_comun:
    print(f"El ancestro común más antiguo entre {nombre1} y {nombre2} es {ancestro_comun.nombre}")
else:
    print(f"No se encontró un ancestro común entre {nombre1} y {nombre2}")
