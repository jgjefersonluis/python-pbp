soma = 0
quantidade = 0

while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 0:
        break;
    soma = soma + n
    quantidade = quantidade + 1
    media = soma/quantidade
print('a quantidade de números digitados: ', quantidade)
print('a soma dos numeros digitados: ', soma)
print('a media dos numeros é %7.2f' %media)

