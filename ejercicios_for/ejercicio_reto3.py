




















numeroPaquetes = int(input())
costoTotal = 0
for i in range(numeroPaquetes):
	alto = float(input())
	ancho = float(input())
	profundo = float(input())
	volumen = alto * ancho * profundo
	costo = volumen * 5
	if alto > 30:
		costo += 2000
	if costo > 10000:
		costo += costo * 0.19
	print(volumen)
	print(costo)
	costoTotal += costo

print(costoTotal)