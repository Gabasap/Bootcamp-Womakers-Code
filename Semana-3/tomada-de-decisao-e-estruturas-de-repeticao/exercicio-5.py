'''
Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero isósceles ou escaleno
equilátero: todos os lados com o mesmo valor
isósceles : dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
'''
print('Vamos classificar este triângulo.')

lado_1 = float(input('Informe o primeiro comprimento: '))
lado_2 = float(input('Informe o segundo comprimento: '))

if lado_1 == lado_2:
    lado_3 = float(input('Informe o terceiro comprimento: '))
    if lado_3 == lado_1:
        print('Este triângulo é equilátero.')
    else:
        print('Este triângulo é isósceles.')
elif lado_1 != lado_2:
    lado_3 = float(input('Informe o terceiro comprimento: '))
    if lado_3 == lado_1:
        print('Este triângulo é isósceles.')
    if lado_3 == lado_2:
        print('Este triângulo é isósceles.')
    else:
        print('Este triângulo é escaleno.')