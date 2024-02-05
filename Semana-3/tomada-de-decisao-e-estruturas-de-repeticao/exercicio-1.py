#Faça um programa que peça dois números e imprima o maior deles.

print('Este programa deve nos dizer o maior número.')

num_1 = float(input('Informe um número: '))
num_2 = float(input('Informe um segundo número: '))

if num_1 > num_2:
    print(f'O primeiro número é o maior. Número {num_1:.2f}.')
elif num_2 > num_1:
    print(f'O segundo número é maior. Número {num_2:.2f}.')