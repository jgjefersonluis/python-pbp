# Escreva um programa calcular consumo energetico
# tipos de instalação R, C e I.
# R = consumo (500) preço 0.40 senao 0.65
# I = consumo (5000) preço 0.55 senao 0.60oc
# C = consumo (1000) preco 0.55 senao 0.60

consumo = int(input('Digite o consumo em Kwh: '))
tipo = input('Tipo de instalação (R, C ou I): ')

# condições

if tipo == 'R':
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == 'I':
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == 'C':
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print('erro! Tipo de instalação é desconhecida')
custo = consumo * preco

print('O valor do consumo será de R$%7.2f reais ' % custo)

