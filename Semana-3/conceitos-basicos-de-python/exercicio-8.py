'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''
print('Vamos calcular o seu salário do mês atual.')

ganho_hora = float(input('Quanto você ganha por hora? '))
hora_trabalhada = float(input('Quantas horas você trabalhou neste mês? '))

salario_mensal = hora_trabalhada*ganho_hora

print(f'O seu salário este mês é de {salario_mensal:.2f} reais.')