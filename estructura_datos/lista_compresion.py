# Convertir una cadena de texto con valores numéricos en una lista 
# con los mismos valores pero convertidos a enteros.
# Forma clasica
# FOR = Lo usamos para recorrer estructuras de datos
values = '32, 45, 11, 87, 20, 48' # También podemos iterarlo (FOR o WHILE)
# Primero sacar los numeros de la cadena de texto y luego
# convertirlos a enteros.
lista = [] # Cree una lista vacia

for i in values.split(', '):
    num_entero = int(numero)
    lista.append(num_entero)

print(lista)


values = '32,45,11'
lis_comp = [int(numero) for numero in values.split(', ')]

print(lis_comp)





# Comprensión 