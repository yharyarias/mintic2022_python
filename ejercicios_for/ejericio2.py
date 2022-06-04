# Escriba un programa que realice las siguientes 9 multiplicaciones.
# 
#               1 * 1
#             1 1 * 1 1
#                 .
#    
#       111111111 * 111111111

uno = "1"
space = 9
for i in range(1, 10): 
    repet = i * uno
    space -= 1
    print(space * " ", repet, "*", repet)
























# one = '1'
# for i in range(1, 10):
#     factor = int(one * i)
#     result = factor * factor
#     print(f'{factor}, '*', factor = result)