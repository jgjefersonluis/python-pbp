# Escreva um programa para calcular a multa do carro que ultrapassou velocidade permitida
# O programa deve exibir o valor de acordo com a multa e tambem se o veiculo não precisara ser multado
# considere: se multa for maior 80 entao a multa será = velocidade - 80 multiplicado por 5, senão a velocidade esta ok!

velocidade = float(input('Digite a velocidade do seu carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print('Você foi multado R$ %7.2f reais. '% multa)

if velocidade <= 80:
    print('A sua velocidade está ok, boa viagem.')