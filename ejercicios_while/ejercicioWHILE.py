# 3. Encontrar el promedio de 5 números usando el ciclo while.
# Salida esperada:
# Ingrese un número: 4 
# Ingrese un número: 7
# Ingrese un número: 22
# Ingrese un número: 6
# Ingrese un número: 3
# El promedio de los números ingesados es: 8.4


# Variables
# Necesitamos una variable
contador = 0
contador2 = 0
numero = 1 # bandera 0 FALSE   1 VERDADERO

# Proceso
# while va hasta que el usuario ingrese el 04
# print() -- Para salir ingresa el número cero
# numero = int(input())
# (5 + 8 + 7 + 10)/CANTIDAD DE NUMERO = PROMEDIO

print("Ingresa cero para cerrar la puerta")
while numero != 0:
    numero = int(input("Ingrese un número: "))
    contador = contador + numero
    contador2 = contador2 + 1
    

# salida
promedio = contador / (contador2-1)
print("El promedio de los valores es: ", promedio)