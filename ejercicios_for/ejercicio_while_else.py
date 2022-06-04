# Tratar de encontrar un multiplo de 9 en el rango 1 a 8

numero = 1

while numero >= 1 and numero <= 100:
    if numero % 9 == 0:
        print("LO ENCONTRAMOS :D ", numero)
    else:
        print("NO LO ENCONTRÉ")
    numero += 1
else:
    print("NO EXISTE MULTIPLO DE 9 EN EL RANGO 1 - 8")









# numero = 8

# while numero >= 1 and numero <=8:
#     if numero % 9 == 0:
#         print("El", numero, "es multiplo de 9")
        
#     numero -= 1
#     print(numero) 
        
# else:
#     print("No es multiplo de 9")

# print("Ha finalizado el ciclo")