# loteria = {56, 12, 14, 14, 34, 26}
# type(loteria)

# conjunto = {}
# print(type(set(conjunto))) # Castear/Parsear

# # Para inicializar un conjunto vacio, declaramos la variable y después del
# # = llamamos a la función/método set()
# conjunto1 = set() # Conjunto vacio


# print(set('tripulantes'))
# Lista a Conjunto
# print(set([2, 3, 3, 5, 6, 12, 5, 1]))
# print(prueba)
# print(sorted(prueba))

# Tupla a Conjunto
# print(set(('ADENINA', 'timina', 'TIMINA', 'GUANINA', 'ADENINA', 'CITOSINA')))

# print(set({'genero':'f', 'telefono': '648780', 'correo':'correo@correo.com'}))

# [1:5]

conjunto = {'ADENINA', 'timina', 'TIMINA', 'GUANINA', 'ADENINA', 'CITOSINA'}
# No permite eliminar elementos por posición pero si por su elemento.
# conjunto.remove('timina')
# conjunto.add('Tripulantes')
# print(conjunto)

# print('ADENINA' in conjunto) # BOOL

# for elemento in conjunto:
#     print(elemento, end=' ')

A = {1, 2} 
B = {2, 3}

# print(A & B)
# print(A.intersection(B))
# print(A | B)
# print(A.union(B))
# print(B - A)
# print(B.difference(A))
print(A ^ B)
print(A.symmetric_difference(B))

