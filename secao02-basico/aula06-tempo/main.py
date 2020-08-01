# Conversão de Horas, Minutos e Segundos em Segundos

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

# minuto tem 60 seg
# uma hora tem 3600 seg / 60 min 60 * 60 = 3600 seg
# dia 24 horas 24 * 3600 seg

total_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos * 60

print('O total de segundos será de %10d '% total_segundos)

