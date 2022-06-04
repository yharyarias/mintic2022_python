import json

def calcularCosto(alto,ancho,profundo):
    volumen = alto * ancho* profundo
    costo = volumen * 5
    if alto > 30:
        costo += 2000
    if costo > 10000:   
        costo *= 1.19 # este tambien funciona costo += costo * 0.19
    return costo

def costoTotal(listaPaquetes, descuento):
    acumulador = 0
    for paquete in listaPaquetes:
        alto = paquete['ALTO']
        ancho = paquete['ANCHO']
        profundo = paquete['PROFUNDO']
        acumulador += calcularCosto(alto, ancho, profundo)
    return acumulador * (1 - descuento / 100)


with open('paquetes.json') as archivo:
	empresa = json.load(archivo)

print(costoTotal(empresa['PAQUETES'], 10))



