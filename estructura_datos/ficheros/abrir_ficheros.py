# RUTA RELATIVA: Ruta corta/ el archivo se encuentra en la misma jerarquia de nuestro py
# RUTA ABSOLUTA: Ruta completa desde la raíz
# \t = Tabular \n = Salto de línea/ Enter
# print(fichero.readlines())

# Escribir sobre ficheros
# w = Write
fichero = open('estructura_datos/ficheros/temps.dat', 'w')
cadena = ('hola', 'como', 'están')
for palabra in cadena: # 23 16
    fichero.write(palabra + '\n')
fichero.close()

f = open('estructura_datos/ficheros/more_data.txt')

# with =  se usa para la apertura en modo lectura
# strip =  Limpiar saltos de línea
# El with se encarga de cerrar nuestro archivo o fichero
with open('estructura_datos/ficheros/temp.txt') as f:
    for line in f: # f es el fichero
        max_temp = line.strip().split()
        print(max_temp)


