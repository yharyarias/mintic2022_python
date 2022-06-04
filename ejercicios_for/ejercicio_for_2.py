# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interes anual y el número de años. Mostrar en pantalla el capital 
# obtenido en la inversión de cada año que dura.
# Capital tras el año 1 es: 468548
# Capital tras el año 2 es: 465658
# Capital tras el año 3 es: 556568



# Variables
capital = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual: "))
tiempo = int(input("Ingrese el tiempo de inversión anual: "))
interes = interes_anual / 100
# Proceso
for i in range(tiempo):
    capital = capital + (capital * (interes))
    # Salida
    print("Capital tras el año", i+1, "es: ", capital)




