# 3. El número dado es de uno o dos dígitos o tres dígitos o más de tres dígitos.
num = int(input("Ingrese un número entero para identificar cuantos digitos tiene: "))


if(num > -10 and num < 10): #  1 2 3 4 5 6 7 8 9
    print("El número", num, "tiene un solo digito")
elif(num > -100 and num  <=-10 or num >= 10 and num < 100):
    print("El número", num, "tiene dos digitos")
elif(num > -1000 and num <= -100 or num >=100 and num < 1000):
    print("El número", num, "tiene tres digitos")
else:
    print("El número", num, "tiene más de tres digitos")
    


