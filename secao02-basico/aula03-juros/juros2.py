# Lucia emprestou R$ 1000,00 reais para sua amiga Márcia mediante uma taxa de 10% ao mes,
# que por sua vez, se comprometeu em pagar a divida num periodo de 1 ano.
# Calcule o valor que Márcia no final pagará para Lucia.


#juros = capital * taxa * tempo

c = 1000
i = 0.10
t = 12
j = c * (i / 100) * t

c = int(input('Digite o valor referente ao capital: '))
i = int(input('Digite a taxa referente ao juros: '))
t = int(input('Digite o tempo: '))

m = c *(1+(i/100*t))

print('O valor total do montante será de R$ {:.2f}'.format(m))