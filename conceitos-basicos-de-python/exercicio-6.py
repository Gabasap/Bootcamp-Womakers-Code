'''
Escreva um programa que calcule o tempo de uma viagem.
Faça um comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
●avião=600km/h
●carro=100km/h
●ônibus=80km/h
'''
print('Vamos calcular o seu tempo de viagem em um:\n- Avião;\n- Carro;\n- Ônibus.')

distancia = float(input('Qual é a distância final da sua viagem em quilômetros? '))

aviao = distancia/600
carro = distancia/100
onibus = distancia/80

print(f'Duração da sua viagem nos seguintes meios de transporte: \nAvião, {aviao:.2f} horas\nCarro, {carro:.2f} horas\nÔnibus, {onibus:.2f} horas')