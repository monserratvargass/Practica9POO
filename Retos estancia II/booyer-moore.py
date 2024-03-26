
#funcion para encontarr el elmento mayoritario presente en una lista dad
def findMajorityElement(nums):
    #crear un hashmap vacio
    d={}
    #almacena la  frecuencia de cada elemento en un diccionario
    for i in nums:
        d[i]=d.get(i,0) + 1
    #devuelve el elemento si se cuenta es mayor que n/2
    for key, value in d.items():
        if value > len(nums)/2:
            return key
    #ningun elemento mayoritario esta presente
    return-1

if __name__=='__main__':

#suposicion # entrada valida (el elemento mayoritario esta presente)
    nums=[1,8,7,4,1,2,2,2,2,2,2]
    result=findMajorityElement(nums)
    if result !=-1:
        print('The majprity element is', result)
    else:
        print('The majority element doesnt exist')

        #pedir datos usando tkinter
        '''parametrso de entrada y salida
        cuantos datos tienes
        ingresar datos 1,2,3 ,n
        retorna #mayoritario y si no lo hay indicar que no hay numero mayoritario'''