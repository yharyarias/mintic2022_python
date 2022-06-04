# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos 
# (utilizando una función que realice dicha suma).

def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
 
num = 1
while num!=0:
    num=int(input("Número a procesar: "))
    print("Suma:",sumaDigitos(num))