# RUTA RELATIVA: corta - Ruta corta para cuando tenemos los archivos
# en la misma jerarquia
# RUTA ABSOLUTA: Larga - cuando tenemos archivos en otros directorios
# usamos la ruta absoluta (desde la raíz)
# \n = salto de línea(enter)

# print(archivo.read())
# print(archivo.readlines())
# read y readlines - Para archivos o ficheros pequeños


# FOR para archivos/ficheros de dimensiones considerables
# for dato in archivo:
#     print(dato)
# Por defecto el ausmen que la acción que va a ejecutar es 'r'
# archivo = open('estructura_datos/ficheros/temps.dat', 'w')

# frutas = ('pera', 'piña', 'manzana')

# for fruta in frutas:
#     archivo.write(fruta + '\n')

# # Evita perder datos - Cierra y guarda
# archivo.close()


# Añadir a un fichero
# archivo = open('estructura_datos/ficheros/temps.dat', 'a')

# # Añade información/atributo al final del fichero
# archivo.write('Hola tripulantes')

# # Evita perder datos - Cierra y guarda
# archivo.close()

# Añadir a un fichero usando with - Añadir texto al final del fichero
with open('estructura_datos/ficheros/temps.dat', 'a') as archivo:
    # Añade información/atributo al final del fichero
    archivo.write('\n' + 'Hola tripulantes')

# Evita perder datos - Cierra y guarda
archivo.close()