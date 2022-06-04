# Solicitar al usuario que ingrese su dirección email.
# Imprimir un mensaje indicando si la dirección es válida o no,
# valiéndose de una función para decidirlo. 
# Una dirección se considerará válida si contiene el símbolo "@". 


def login(email):
    simbolo = "@"
    for i in email: # Es para recorrer toda la cadena de texto}
        if i == simbolo:
            return True
    return False
    
email = input("Ingrese su correo: ")
if login(email):# TRUE
    print("Pertenece a un correo")
else: # FALSE
    print("No pertence a un correo")