'''
Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão.... 
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo também e estou migrando de área.
'''
nome = str(input('Qual o seu nome? '))
idade = int(input('Quantos anos você tem? Apenas números. '))
livro = str(input('Qual seu livro preferido? '))
cor = str(input('Qual sua cor preferida? '))

print(f'Olã, {nome}, de {idade} anos.\nVocê gosta de {livro} e da cor {cor}.')