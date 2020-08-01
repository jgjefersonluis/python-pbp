# Crie um programa que leia um valor em quilometros e quantidades
# de dias que usou o veiculo, o valor a ser cobrado por dia sera de
# R$ 60,00 e o valor por Km será de R$ 0,15.

km = int(input('Digite a quantidade de Km rodados: '))
dias = int(input('Digite o valor dos dias rodados: '))
preco_dia = 60
preco_km = 0.15
preco_pagar = km * preco_km + dias * preco_dia

print('O total a pagar será de R$ %5.2f ' % preco_pagar)

