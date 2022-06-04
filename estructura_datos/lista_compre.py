# Convertir una cadena de texto con valores númericos en
# una lista con los mismos valores pero convertidos a 
# enteros. 

# valores = '56,35,6,10'
# lista = [] # Lista vacia

# for numero in valores.split(','):
#     int_num = int(numero)
#     lista.append(int_num) # Añadiendo los iten(Los números) a la lista
#     # Siempre que queramos añadir datos a una lista vacia
#     # o llena, usamos append
# print(lista)

valores = '56,35,6,10'
lista = [int(numero) for numero in valores.split(',')]
print(lista)




