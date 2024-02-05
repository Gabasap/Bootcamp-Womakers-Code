'''
Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
'''
from datetime import date

print('Este programa deve informar a sua idade atual.')

nasc = int(input('Digite o seu ano de nascimento: '))
ano = date.today()

idade = ano.year - nasc
print(f'Você tem atualmente {idade} anos.')