'''
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.
'''
print('Vamos calcular o total de calorias que você queimou nesta semana.')

horas_exerc = float(input('Quantas horas de exercício físico você fez nesta semana? '))
minutos_exerc = horas_exerc*60
total_kcal = minutos_exerc*5

print(f'Total de calorias gastas na semana: {total_kcal:.2f} kcal.')