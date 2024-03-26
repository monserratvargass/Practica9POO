from random import randrange
#funcion de utilidad para intercambia A[I] Y A[J] en una lista

def swap(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp

    #funcion para bajarar una lista A

def shuffle(A):
    #Lista de lectura desde el indice mas najo hasta el mas alto
    for i in range(len(A)-1):
        #genera un numero aleatorio j tal que i<=j<n
        j=randrange(i,len(A))

        #intercambia el elemento actual con el indice generando aleatoriamente
        swap(A,i,j)

if __name__=='__main__':
    A=[1,2,3,4,5,6]
    shuffle(A)

    #imprime la lista barajada
    print(A)

    '''SOBRE EL MISMO PROGRAMA: hacer una ventana para entrada de datos
    debe pedir el numero de datos y despues otra vemtana donde ingrese
    dato por dato
    
    imprimir el resultado en una ventana con los datos en la fila separadas
    por comas'''