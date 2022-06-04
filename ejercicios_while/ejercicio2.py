# 3. Leer un número entero positivo desde teclado e 
# imprimir la suma de los dígitos que lo componen.

# Variables
numero = int(input("Ingrese un número entero positivo: "))
contador = 0 # Los contadores por lo general se inicializan en cero

# Proceso
while numero > 0: 
    digito = numero % 10 
    contador += digito
    numero //= 10
# Salida
print("La suma total de los digitos es: ", contador)


















    

