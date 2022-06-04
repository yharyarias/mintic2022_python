# El número dado es par o impar.


# num = -> Declarar una variable
# int() -> Castear
# input(STRING) -> Leimos el dato o solicitamos un dato
num = int(input("Ingrese un número entero para identificar si es par o impar: "))

# print("El número es par")
# print("El número es impar")

if(num % 2 == 0):
    print("El número", num, "es par")
else:
    print("El número", num, "es impar")