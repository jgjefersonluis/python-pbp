
def main():
    nome = input('Digite o nome do procurado: ')
    crime = input('Digite o crime cometido pelo produrado: ')
    data_nasc = input('Digite a data de nascimento do procurado: ')
    idade_atual = input('Digite a idade atual do procurado: ')
    nasceu = input ('Digite a cidade de nascimento do procurado: ')
    sexo = input('Digite o sexo do procurado: ')
    pele = input('Digite a cor da pele do procurado: ')
    olhos = input('Digite a cor dos olhos do procurado: ')
    cabelo = input('Digite a cor do cabelo do procurado: ')
    altura = input('Digite a altura do procurado: ')
    tatu_cicatriz = input('Digite se existem tatuagens e cicatrizes no procurado: ')

    print()
    print(f"PROCURADO PELA POLICIA EM TODO TERRITORIO NACIONAL")
    print('Nome: ', nome)
    print('Crime: ', crime)
    print('Data de nascimento: ', data_nasc)
    print('Idade atual: ', idade_atual, 'anos.')
    print('Natural de: ', nasceu)
    print('Sexo: ', sexo)
    print('Cor da pele: ', pele)
    print('Cor dos olhos: ', olhos)
    print('Cor do cabelo: ', cabelo)
    print('Altura: ', altura, 'metros.')
    print('Tatuagens e cicatrizes: ', tatu_cicatriz)

main()