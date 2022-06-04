alto = float(input())
ancho = float(input())
profundo = float(input())

volumen = alto * ancho * profundo
costo = volumen * 5

if(alto > 30):
    costo = costo + 2000

if(costo > 10000):
    costo = costo * 1.19

print(volumen)
print(costo)











