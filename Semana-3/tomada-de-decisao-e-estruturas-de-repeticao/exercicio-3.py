'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
nota = float(input('Informe uma nota entre zero e dez: '))

while nota >= 11:
    print('Valor inválido')
    nota = float(input('Digite novamente: '))
else:
    print('Valor válido')