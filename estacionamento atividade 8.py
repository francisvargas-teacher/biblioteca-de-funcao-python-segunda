# Matriz do estacionamento

estacionamento = [
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0]
]


# Funcao para estacionar

def estacionar(matriz, linha, coluna):
    if matriz[linha][coluna] == 0:
        matriz[linha][coluna] = 1
        print('Veiculo estacionado com sucesso!')
    else:
        print('Essa vaga ja esta ocupada!')


# Funcao para retirar veiculo

def retirar_veiculo(matriz, linha, coluna):
    if matriz[linha][coluna] == 1:
        matriz[linha][coluna] = 0
        print('Veiculo retirado com sucesso!')
    else:
        print('Essa vaga ja esta livre!')


# Funcao para consultar vagas

def consultar_vagas(matriz):
    total = 0
    maior = 0
    fileira = 0

    for i in range(len(matriz)):
        livres = 0

        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                total += 1
                livres += 1

        if livres > maior:
            maior = livres
            fileira = i + 1

    print('Total de vagas livres:', total)
    print('Fileira com mais vagas livres:', fileira)
    print('Quantidade de vagas livres:', maior)


# Menu principal

while True:
    print('\n===== ESTACIONAMENTO =====')
    print('1 - Estacionar veiculo')
    print('2 - Retirar veiculo')
    print('3 - Consultar vagas')
    print('4 - Mostrar estacionamento')
    print('5 - Sair')

    opcao = input('Escolha uma opcao: ')

    if opcao == '1':
        linha = int(input('Digite a fileira (1 a 4): '))
        coluna = int(input('Digite a vaga (1 a 5): '))

        if 1 <= linha <= 4 and 1 <= coluna <= 5:
            estacionar(estacionamento, linha - 1, coluna - 1)
        else:
            print('Fileira ou vaga invalida!')

    elif opcao == '2':
        linha = int(input('Digite a fileira (1 a 4): '))
        coluna = int(input('Digite a vaga (1 a 5): '))

        if 1 <= linha <= 4 and 1 <= coluna <= 5:
            retirar_veiculo(estacionamento, linha - 1, coluna - 1)
        else:
            print('Fileira ou vaga invalida!')

    elif opcao == '3':
        consultar_vagas(estacionamento)

    elif opcao == '4':
        for linha in estacionamento:
            print(linha)

    elif opcao == '5':
        print('Programa encerrado!')
        break

    else:
        print('Opcao invalida! Tente novamente.')

