# Escreva um programa calcular o financiamento de uma casa
# Sera necessario informar o salario, o valor da casa e quantidad em anos.
# Sabendo que a prestação sera o valor pelos anos. Se a prestação for maior que
# O salario vezes o 0.30 a prestação nao sera aceita.

valor = float(input('Digite o valor  da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite anos a pagar: '))
meses = anos * 12
prestacao = valor/meses

# condição

if prestacao > salario * 0.30:
    print('O seu financiamento não foi aprovado.')
else:
    print('O seu financiamento foi aprovado, parabéns!')
    print('O valor da prestação será de R$%7.2f reais '% prestacao)

