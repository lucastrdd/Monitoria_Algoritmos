'''
Implemente um código para criar uma matriz transposta.
'''


def transposta(matriz):
    vetor = []

    for k in range(len(matriz[0])):
        vetor.append([])

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            vetor[j].append(matriz[i][j])

    return vetor


def print_matriz(matriz):
    for i in range(len(matriz)):
        print("[ ", end='')
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]}, ", end='')
        print(" ]")


mat1 = [[1, 2, 3], [4, 5, 6]]
mat2 = transposta(mat1)

print_matriz(mat1)
print()
print_matriz(mat2)
