# Escreva um programa para exibir as 4 operaçoes matematicas onde o usuario escolhera a que sera usada
# lembrando que o usuario digitara somente dois valores

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

operacao = input('Digite a operação a ser utilizada(+,-,* ou /) : ')

# condições

if operacao == '+':
    resultado = a + b
elif operacao == '-':
    resultado = a - b
elif operacao == '*':
    resultado = a * b
elif operacao == '/':
    resultado = a / b
else:
    print('operação invalida!')
    resultado = 0

print('Resultado: %7.2f ' %resultado)
