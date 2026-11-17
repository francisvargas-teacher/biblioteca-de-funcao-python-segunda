
# Exercicio 3 - Rotacionar uma matriz 90 graus
# Objetivo: girar uma matriz 90 graus no sentido horario


# Funcao responsavel por rotacionar a matriz
def rotacionar_matriz_90(matriz):

    # Descobre a quantidade de linhas da matriz original
    linhas = len(matriz)

    # Descobre a quantidade de colunas da matriz original
    colunas = len(matriz[0])

    # Cria uma nova matriz com as dimensoes invertidas
    # Exemplo: uma matriz 2x3 passa a ser 3x2
    # Inicialmente, todas as posicoes recebem zero
    rotacionada = [
        [0 for j in range(linhas)]
        for i in range(colunas)
    ]

    # Primeiro for: percorre as linhas da matriz original
    for i in range(linhas):

        # Segundo for: percorre as colunas da matriz original
        for j in range(colunas):

            # Coloca cada elemento na nova posicao
            # O indice j passa a representar a nova linha
            # A expressao linhas - 1 - i inverte a ordem
            # das linhas originais nas colunas da nova matriz
            rotacionada[j][linhas - 1 - i] = matriz[i][j]

    # Retorna a matriz rotacionada
    return rotacionada


# Cria a matriz original com 2 linhas e 3 colunas
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Chama a funcao e armazena o resultado
resultado = rotacionar_matriz_90(matriz)

# Mostra a matriz original
print("Matriz original:")
for linha in matriz:
    print(linha)

# Mostra a matriz depois da rotacao
print("\nMatriz rotacionada 90 graus:")
for linha in resultado:
    print(linha)
