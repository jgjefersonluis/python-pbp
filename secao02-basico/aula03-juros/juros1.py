# Uma pessoa empresta R$ 3000,00 a uma taxa de juros simples de 3% ao mês
# em um periodo de 5 meses. Quanto receberá ao final desse periodo.

c = int(input('Digite o valor referente ao capital: '))
i = int(input('Digite a taxa referente ao juros: '))
t = int(input('Digite o tempo: '))

j = c * (i / 100) * t
m = c + j

# m = c * (1 + (i/100*t)) tambem poderia ser utilizado

print('O valor total do montante será de R$ {:.2f}'.format(m))
