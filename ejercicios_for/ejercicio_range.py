# Perdir al usuaro que ingrese un número entero positivo 
# e imprimir todos los números correlativos, entre el ingresado 
# por el usuario y uno menos del doble del mismo


numero = int(input("Ingrese un número entero: "))


for i in range(numero, numero*2):
    print(i, end = ' ')

