# Reto 4

# Variables
# Proceso 
# Salida

#########################################################################

# Variable (opcional)
# Funciones - Proceso
# Pedir variables
# Proceso
# Salida - Llamar las funciones y pasarle los parametros que necesite

def calcularCosto(alto, ancho, profundo):
    volumen = alto * ancho * profundo
    costo = volumen * 5
    if alto > 30:
        costo += 2000
    if costo > 10000:
        costo *= 1.19
    return costo

def costoTotal(numeroPaquetes, descuento):
    acumulador = 0
    for i in range(numeroPaquetes):
        alto = float(input())
        ancho = float(input())
        profundo = float(input())
        acumulador += calcularCosto(alto, ancho, profundo)
    return acumulador * (1 - descuento / 100)
# Podemos asignar como valor a una variable
# una función
# variable = costoTotal(6, 10)

print(costoTotal(2, 10))


        


