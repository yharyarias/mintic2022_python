# Solicitar números al usuario hasta que ingrese el cero. 
# Por cada uno, mostrar la suma de sus dígitos 
# (utilizando una función que realice dicha suma).


def suma(numero1):
    valor = 0  # Contadores / acumuladores 32
    while numero1 != 0:
        digito = numero1 % 10
        valor += digito
        numero1 //= 10
    return valor

num = 1 # Bandera
while num != 0:
    num = int(input("Ingrese un número (para finalizar, ingrese el cero): "))
    print("La suma de los digitos es: ", suma(num))

