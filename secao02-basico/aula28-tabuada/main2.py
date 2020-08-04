# Faça uma tabuada
# versão 2.0

n = int(input('Tabuada de: '))
inicio = int(input('De: '))
fim = int(input('Até: '))

a = inicio

while a <= fim:
    print('%d X %d = %d ' %(n, a, n*a))
    a = a + 1

