# Dado un número entero (leer el número o darle un valor) identificar cuantos digitos tiene
# imprimir en pantalla los que tienen un digito o dos digitos o tres digitos o más de tres digitos.
# --------------------------------------------------------------------------------------------------
# Declarar variables y si es necesario solicitar datos

# Proceso - operaciones - condicionales - ciclos

# Salida - print() - return
# input() - convierte los datos que lee en string (cadena de texto)
# Si necesitamos el tipo de dato diferente a str, lo casteamos.

numero = int(input("Ingrese un número para identificar su digitos: "))

# Más cerca del cero MAYOR
# Más lejos del cero MENOR
# or solo se pide que cumpla una condicion
# and cumpla 2 condiciones


if(numero > -10 and numero < 10): # 0 1 2 3 4 5 6 ...9
    print("El número", numero, "tiene un digito")
elif(numero > -100 and numero <= -10 or numero >= 10 and numero < 100): # 10......99
    print("El número", numero, "tiene dos digitos")
elif(numero > -1000 and numero <= -100 or numero >=100 and numero < 1000): # 100 101 ..... 999
    print("El número", numero, "tiene tres digitos")
else: # 1000 .....
    print("El número", numero, "tiene más de tres digitos")









