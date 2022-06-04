# Objeto en Python: Cuando creas una variable y le asignas
# un valor, una función también es un objeto, listas, tuplas
# diccionario, cadena texto/caracteres.... OBJETO
# VERACIDAD
# Verificar que sea VERDADERO o FALSO los parametros 
# que le pasamos a una función/método.


def veracidad(objeto):
    if objeto: # True
        print(objeto, 'es TRUE')
    else: # False
        print(f'{objeto} es FALSE')

# veracidad(False)
# veracidad(None)
# veracidad(0)
# veracidad(0.0)
# veracidad('')
# veracidad([]) # Lista
# veracidad(()) # Tupla
# veracidad({}) # Diccionarios
# veracidad(set()) # Conjunto NO REPITE DATOS


