# Listas

# mi_lista = [] # Inicializar una lista vacia
# ciudades = ['Bogotá', 'Cali', 'Medellín'] # Lista de elementos de tipo String
# numeros = [1, 2, 3, 4] # Lista de enteros
# lista_mix = ['Bucaramanga', {'nombre':'Estefania', 'edad':26}, 6258, (2.6, 3.9)]
# El segundo elemento es un diccionario
# El ultimo elemento es una tupla

# print(list('tripulantes'))
# Los string/cadenas de texto son datos iterables

# mi_lista = ['hola', 'como', 'estás']
# print(mi_lista[0], mi_lista[1:3])

# shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
# print(shopping[-3:-5:-1]) # 
# print(shopping[::-2]) # Sal y Huevos
# print(shopping[3::1])# Sal y Huevos --- start:stop:step(Atrás - NEGATIVO)
# print(shopping[-2::-2]) # Sal y Huevos ----- start:stop:step(Restando desde el número que incia- NEGATIVO)
# print(shopping[:1:-1]) # Hace lo mismo (Sal y Huevos)
# print(shopping[5]) # Posición exacta


# lista_fruit = ['manzana', [1, 3], 2]
# lista_fruit[1].pop()

# print(lista_fruit)

# frutas = ['Fresa', 'Manzana', 'Lulo', 'Melón']

# print('Fresa' and 'Manzana' in frutas)



# JOIN

shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
frutas = ['Fresa', 'Manzana', 'Lulo', 'Melón']
lista = ['Casa', 'Sala', 'comedor', 'Sala']

print(frutas)
frutas.sort(reverse=True) # Sort modifica la lista
print(frutas)
sorted(frutas, reverse=True)
frutas_mod = sorted(frutas, reverse=True) # ordena de Z - A --- Conserva la lista original.
print(frutas)

# SORT - MODIFICA LA LISTA ORIGINAL
m = 5
m = 10
# SORTED - CONSERVA LA LISTA ORIGINAL









