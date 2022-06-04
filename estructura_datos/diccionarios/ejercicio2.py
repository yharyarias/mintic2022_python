# Usando un diccionario, cuente el número de veces que
# se repite cada letra en una cadena de texto.

# Entre: 'especificamente'
# Salida: {'e':4, 's':1, 'p':1, 'c':2, 'i':2, 'f':1, a':1, 'm':1, 'n':1, 't':1}

oracion = 'especificamente'

contador_letras = {}

for letra in oracion:
    if letra in contador_letras:
        contador_letras[letra] += 1
    else:
        contador_letras[letra] = 1

# print(contador_letras)
# print(contador_letras.values())
# print(contador_letras.items())
# print(len(contador_letras))

print(contador_letras.setdefault('e'))
contador_letras = {valor for valor in contador_letras.values()}
print(contador_letras)
# for valor in contador_letras.values():
#     print(valor)

