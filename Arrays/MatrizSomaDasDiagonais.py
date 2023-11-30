'''
Escreva um código para calcular a soma dos elementos nas diagonais principal e secundária de uma matriz quadrada.
'''


def soma(matriz):
    primaria = 0
    secundaria = 0

    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            if (l == c):
                primaria += matriz[l][c]
            elif ((l+c) == len(matriz) - 1):
                secundaria += matriz[l][c]

    return primaria + secundaria


mat = [[1, 0, 0, 0, 1],
       [0, 1, 0, 1, 0],
       [0, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 0, 0, 1]]

print(soma(mat))