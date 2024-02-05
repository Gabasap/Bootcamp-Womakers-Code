'''
Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l
'''
print ('Olá, novo usuário.\nNeste exercício vamos calcular o seu consumo médio de combustível por quilometro rodado.')

litro = float(input('Quantos litros de combustível foram consumidos no seu trajeto? '))
print (f'{litro:.2f} litros')

km = float(input('Agora me diga, qual foi a distância percorrida? '))
print (f'{km:.2f} quilometros')

consumo = km/litro
print (f'\nTudo pronto, o seu consumo médio foi de {consumo} KM/L.')