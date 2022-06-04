# Solicitar al usuario que ingrese su dirección email.
# Imprimir un mensaje indicando si la dirección es válida o no,
# valiéndose de una función para decidirlo. 
# Una dirección se considerará válida si contiene el símbolo "@".

def validar(email):
    caracterBuscado="@"
    #emailValido=False
    for c in email:
        if c==caracterBuscado:
            return True
    return False


direccion=input("Tu email: ")
if validar(direccion): # TRUE
    print("Dirección válida")
else:
    print("Dirección inválida")