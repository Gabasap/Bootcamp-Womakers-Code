'''
Solicite ao usuário o peso em kg e a altura em metros.
Calcule e imprima o Índice de Massa Corporal(IMC) usando a fórmula: IMC=peso/(altura x altura).
'''
print('Vamos calcular o seu IMC ou Índice de Massa Corporal.')

peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em metros: '))

imc = peso/(altura*altura)

print(f'Seu IMC é de {imc:.2f}')