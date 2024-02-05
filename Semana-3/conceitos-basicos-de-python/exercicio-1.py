'''
1. Faça um programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão.
'''

print("Este programa apresentará um resultado numérico com base em quatro operadores matemáticos: \n -Adição; \n -Subtração; \n -Divisão; \n -Multiplicação. ")

num1 = float(input(f'Informe o primeiro número: '))
num2 = float(input(f'Informe o segundo número: '))

soma = num1+num2
print(f'Este é o resultado da soma: {soma:.2f}')

sub = num1-num2
print(f'Este é o resultado da subtração: {sub:.2f}')

div = num1/num2
print(f'Este é o resultado da divisão: {div:.2f}')

mult = num1*num2
print(f'Este é o resultado da multiplicação: {mult:.2f}')