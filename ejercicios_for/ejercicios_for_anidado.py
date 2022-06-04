# Escribir un programa que pida al usuario un número entero y muestre
# por pantalla un triangulo rectangulo como el de más abajo, de altura
# el número introducido.

# n = 9

# 1            
# 3 1         
# 5 3 1        
# 7 5 3 1     
# 9 7 5 3 1   

# Variables
numero = int(input("Ingrese la altura del triangulo: "))

# Proceso
for i in range(numero):
    for j in range(i, 0,-1):
        # Salida
        print(j, end = " ")
    # Salida
    print("")
    









