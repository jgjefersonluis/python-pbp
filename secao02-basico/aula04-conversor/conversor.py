# Conversor de medidas
# metros para milimitros
# metros para quilometros

print('Conversor de medidas')

metros = float(input('O valor em metros: '))
milimetros = metros * 1000
quilometros = metros / 1000

print('O valor de {%10.0f} metros é de %10.0f milimetros ' % (metros, milimetros))

print('O valor de {%10.0f} metros é de %10.0f quilometros ' % (metros, quilometros))