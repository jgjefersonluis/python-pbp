# Calcule o tempo de uma viagem de carro. Pergunte a distancia
# a percorrer e a velocidade media esperada para a viagem

distancia = float(input('Digite o valor da distancia em Km: '))
velocidade_media = float(input('Digite o valor da velocidade media em Km/h: '))
tempo = distancia/velocidade_media

print('O tempo estimado será de %5.2f horas '% tempo)

