# Solicitar al usuario que ingrese su dirección email.
# Imprimir un mensaje indicando si la dirección es válida o no,
# valiéndose de una función para decidirlo. 
# Una dirección se considerará válida si contiene el símbolo "@". 

def validar_email(email):
    arroba = "@"
    for i in email:
        if i == arroba:
            print("Dirección email correcta")
            break
        else:
            print("Dirección email incorrecta")
            
correo = input("Ingresa tu correo: ")
print(validar_email(correo))