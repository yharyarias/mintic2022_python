# Escribir un programa que guarde en una variable el
# diccionario {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}, 
# pregunte al usuario por su divisa y muestre su simbolo
# o un mensaje de aviso si la divisa no está en el diccionario

# 1. Variable
# 2. input
# 3. if

monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
divisa = input("Ingrese su moneda local: ")
# Necesitamos imprimir el valor 

if divisa in monedas:
    print(monedas.get(divisa))
else:
    print('no está en el diccionario')

