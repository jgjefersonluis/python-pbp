# Escreva um programa para exibir o maior e menor valor uma vez digitado pelo usuario

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

maior = a
if b > c and b > a:
    maior = b
if c > b and c > a:
    maior = c

menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c

print('O menor valor é %d : ' % menor)
print('O maior valor é %d : ' % maior)

