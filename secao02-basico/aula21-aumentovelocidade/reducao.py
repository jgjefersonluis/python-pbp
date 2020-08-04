# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele ja fumou.
# Considere que o fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perdera.
# Exiba o total em dias.

cigarros_dia = int(input('Quantidade de cigarros por dia: '))
anos_fumando = float(input('Quantidade de anos fumando: '))
reducao_minutos = anos_fumando * 365 * cigarros_dia * 10
reducao_dias = reducao_minutos / (24 * 60)

print('Redução do tempo de vida em dias será de %8.0f dias. ' % reducao_dias)
