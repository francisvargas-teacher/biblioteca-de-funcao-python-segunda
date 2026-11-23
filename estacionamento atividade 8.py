# Funcao para consultar vagas

def consultar_vagas(matriz):
    total = 0
    ocupadas = 0
    maior = 0
    fileira = 0

    for i in range(len(matriz)):
        livres = 0

        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                total += 1
                livres += 1
            else:
                ocupadas += 1

        if livres > maior:
            maior = livres
            fileira = i + 1

    print('Total de vagas livres:', total)
    print('Total de vagas ocupadas:', ocupadas)
    print('Fileira com mais vagas livres:', fileira)
    print('Quantidade de vagas livres:', maior)