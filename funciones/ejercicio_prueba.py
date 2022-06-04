# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos 
# (utilizando una función que realice dicha suma).

def sumaDig(numero, v):
    cont = 0
    while numero != 0:
        digito = numero % 10 # Saca el ultimo digito 2
        cont += digito
        numero //= 10
    return cont

num = int(input("Ingrese un número: "))
if num > 0:
    print("La suma de los digitos es: ", sumaDig(num))


