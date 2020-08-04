# Escreva um programa para calcular aumento salarial, se o valor do salario for maior que R$ 1200,00
# o percentual de aumento será de 10% senao sera de 15%.

salario = float(input('Digite o seu salario: '))

# condições

if salario > 1200:
    pc_aumento = 0.10
    aumento = salario * pc_aumento
if salario <= 1200:
    pc_aumento = 0.15
    aumento = salario * pc_aumento

print('O seu aumento salarial é de R$ %7.2f reais. ' %aumento)

