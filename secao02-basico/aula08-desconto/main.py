# crie um programa que leia um preço de uma mercadoria
# também adicione um percentual de desconto

preco = float(input('Digite o preço da mercadoria: '))
desconto = float(input('Digite o percentual de desconto: '))
valor_desconto = preco * desconto/100
pagar = preco - valor_desconto

print('O desconto será de R$ %5.2f ' % valor_desconto)
print('O valor a seer pago será de R$ %5.2f ' %pagar)
