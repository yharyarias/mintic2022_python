# Escribir un programa que pida números positivos al usuario. 
# Mostrar el número cuya sumatoria de dígitos fue mayor 10 y la 
# cantidad de números cuya sumatoria de dígitos fue menor que 10. 

def sumaDig(numero):
    suma = 0 # Contador/Acumulador = 0
    while numero != 0: # 32----3
        digito = numero % 10 # 2----- 3
        suma += digito  # 0 + 2 ---- 2 + 3 = 5
        numero //=10 # 32//10 = 3----- 3 //10 = 0
    return suma

numero = 1 # Bandera
contador = 0
while numero != 0:
    numero = int(input("Ingrese un número positivo: "))
    if numero == 0:
        break
    sumatoria = sumaDig(numero) # Retorna la suma de los digitos
    if sumatoria < 10:
        contador += 1
        print("Cantidad de número < 10 son: ", contador , " es menor que  10, la suma es: ", sumatoria)
    if sumatoria >= 10:
        print("la sumatoria de este numero: ", numero , " es mayor que  10, la suma es: ", sumatoria)













