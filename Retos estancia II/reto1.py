multiplo = int(input("Por favor, ingresa un número del 1 al 100: "))

if multiplo % 3 == 0 and multiplo % 5 == 0:
    print("Hola Mundo")
elif multiplo % 3 == 0:
    print("Hola")
elif multiplo % 5 == 0:
    print("Mundo")
else:
    print(multiplo)

