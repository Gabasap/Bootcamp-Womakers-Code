'''Desenvolver um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.
'''
idade = int(input('Quantos anos você tem? '))

if idade <= 12:
    print('Criança.')
elif idade <= 20:
    print('Adolescente.')
elif idade <= 60:
    print('Adulto.')
else:
    print('Idoso.')