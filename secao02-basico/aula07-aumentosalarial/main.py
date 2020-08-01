# crie um programa que leia e execute um valor e acrescente
# seu percentual de aumento

salario = float(input('Digite o salario atual: '))
p_aumento = float(input('Digite a porcentagem de aumento: '))
aumento = salario * p_aumento/100
salario_novo = salario + aumento

print('O valor do aumento será de R$ %7.2f ' % aumento)
print('O novo salario será de R$ %7.2f ' % salario_novo)
