'''
Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.
'''
print('Este programa deve transformar a quilometragem oferecida em: \n- Metros; \n- Centímetros; \n- Milímetros.')

km = float(input('Informe a quilometragem a ser convertida: '))

metro = km*1000
print(f'Este é o resultado em metros: {metro:.2f} metros.')

cent = km*100000
print(f'Este é o resultado em centímetros: {cent:.2f} centímetros.')

mili = km*1000000
print(f'Este é o resultado em milímetros: {mili:.2f} milímetros.')
