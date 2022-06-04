# Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, 
# al finalizar, la cantidad total de números leídos. Utilizar una o más funciones, 
# según sea necesario.

def factorial(n):
    fact = 1 # Contador / Acumulador
    for i in range(1, n + 1):
        fact = fact * i
    return fact
    

num = 1 # Bandera
cont = 0 # Contador
while num != 0:
    num = int(input("Ingrese un número (Para cerrar ingrese el 0):"))
    if num == 0:
        break
    cont += 1
    print("El factorial del número", num, "es", factorial(num))

print("Se ingresaron", cont, "números")


















        










