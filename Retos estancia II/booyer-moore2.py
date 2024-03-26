def findMajorityElement(nums):
    # Crear un diccionario vacío para almacenar las frecuencias de los elementos.
    d = {}
    
    # Calcular la frecuencia de cada elemento en la lista.
    for i in nums:
        d[i] = d.get(i, 0) + 1
    
    # Buscar si hay algún elemento con una frecuencia mayor que la mitad del tamaño de la lista.
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    
    # Si no se encontró ningún elemento mayoritario, devuelve -1.
    return -1

if __name__ == '__main__':
    # Solicitar al usuario ingresar una lista de números separados por comas
    input_nums = input('Ingrese una lista de números separados por comas: ')
    
    # Convertir la entrada del usuario en una lista de números
    nums = [int(x) for x in input_nums.split(',')]
    
    result = findMajorityElement(nums)
    
    if result != -1:
        print('El elemento mayoritario es', result)
    else:
        print('El elemento mayoritario no existe')
