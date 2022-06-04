palabras = ('marte', 'tierra', 'jupiter', 'saturno')
# LLAVES de los diccionarios
dic_planetas = {planeta:len(planeta) for planeta in palabras}
print(dic_planetas)























# rae1 = {
#     'bifronte': 'De dos frentes o dos caras',
#     'enjuiciar': 'Someter una cuestión a examen, discusión y juicio'
# }

# rae2 = {
#     'anarcoide': 'Que tiende al desorden',
#     'montuvio': 'Campesino de la costa',
#     'enjuiciar': 'Instruir, juzgar o sentenciar una causa'
# }




# NO USAR HASH EN DICCIONARIOS
# rae2.update(rae1)
# print(rae2)
# rae1.update(rae2)
# print(rae2)
#rae2.update(rae1)

# rae1 = rae1 + rae2
# rae2 = rae1 + rae2 + rae2


# Cuando dos llaves se repiten, deja solo una llave y se trae su ultimo valor
# print({**rae1,**rae2})

# un * une solo las llaves
# dos * une llaves y valores
# rae1.update(rae2)
# print(rae1)
# print(rae2)
# rae2.update(rae1)
# print(rae2)