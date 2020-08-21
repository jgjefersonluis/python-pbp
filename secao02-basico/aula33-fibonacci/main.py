# def
# Fibonacci

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
num = int(input('digite um numero encontrar seu fibonacci: '))

resposta = fibo(num-1)

print(resposta)
