# FOR
# Escribir un programa que pida al usuario un número entero positivo y muestre 
# en pantalla la cuenta hacia atrás desde ese número hasta cero, separados por comas.

# Variables
numero = int(input("Ingresa un número entero:"))

# Proceso 
for i in range(numero, -1, -1):
    # Salida
    print(i, end = ',')




