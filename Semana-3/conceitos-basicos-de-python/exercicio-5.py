'''
Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
●Renda até R$1.903,98: isento de imposto de renda;
●Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%;
●Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%;
●Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%;
●Renda acima de R$4.664,68: alíquota máxima de27,5%
'''
print('Com este programa seu salário líquido será calculado.')

salario_bruto = float(input('Informe seu salário bruto: '))

if salario_bruto <= 1903.98:
    print(f'Seu salário líquido é de R${salario_bruto:.2f} reais.')

elif salario_bruto <= 2826.65:
    salario_liq_1 = salario_bruto - 158.40
    print(f'Seu salário líquido é de R${salario_liq_1:.2f} reais.')

elif salario_bruto <= 3751.05:
    salario_liq_2 = salario_bruto - 370.40
    print(f'Seu salário líquido é de R${salario_liq_2:.2f} reais.')

elif salario_bruto <= 4664.68:
    salario_liq_3 = salario_bruto - 651.73
    print(f'Seu salário líquido é de R${salario_liq_3:.2f} reais.')

elif salario_bruto >= 4664.69:
    salario_liq_4 = salario_bruto - 884.96
    print(f'Seu salário líquido é de R${salario_liq_4:.2f} reais.')