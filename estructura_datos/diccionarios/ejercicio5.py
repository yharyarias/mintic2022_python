formulario = {'nonbre':'Sofia', 'edad':25, 'genero':'f', 'id':123456}

# Imprimir todas claves del diccionario y escribir los valores.
# -----
# diccionario
# for 
# keys()

for clave, valor in formulario.items(): # ((nombre, Sofia), (edad, 25), (genero, f), (id, 123456))
    print(f"{clave}: {valor}")


# print('con la función ', formulario.values())
# for clave in formulario.values():
#    print(clave)
