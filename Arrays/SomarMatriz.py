'''
Crie duas matrizes e escreva um código para calcular a soma delas.
'''


def somar_mat(mat1, mat2):
    vetor = []

    for k in range(len(mat1)):
        vetor.append([0]*len(mat1[0]))

    for i in range(len(vetor)):
        for j in range(len(vetor[0])):
            vetor[i][j] = mat1[i][j] + mat2[i][j]

    return vetor


def print_matriz(matriz):
    for i in range(len(matriz)):
        print("[ ", end='')
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]} ", end='')
        print(" ]")


matriz1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
matriz2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

soma = somar_mat(matriz1, matriz2)
print_matriz(soma)
