T=[-10,-8,0,1,2,5,-2,-4]
mínima = T[0]
máxima = T[0]
soma = 0

for e in T:
    if e < mínima:
        mínima = e
    if e > máxima:
        máxima = e

soma = soma + e

print("Temperatura máxima: %d °C" %máxima)
print("Temperatura mínima: %d °C" %mínima)
print("Temperatura média: %d °C" %(soma / len(T)))
