'''
Escreva um código para trocar duas linhas em uma matriz.
'''
from random import randint


def criar(l, c):
    vetor = []
    for i in range(l):
        vetor.append([])
        for j in range(c):
            vetor[i].append(randint(0, 9))
    return vetor


def print_matriz(matriz):
    for i in range(len(matriz)):
        print("[ ", end='')
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end='')
            if j < len(matriz[i]) - 1:
                print(", ", end='')
        print(" ]")


def trocar(mat, lin1, lin2):
    lin1 -= 1
    lin2 -= 1
    aux = mat[lin1]
    mat[lin1] = mat[lin2]
    mat[lin2] = aux
    return mat


linhas = int(input("Quantas linhas deve ter a matriz? "))
colunas = int(input("Quantas colunas deve ter a matriz? "))
matriz = criar(linhas, colunas)
print_matriz(matriz)

linhas, colunas = map(int, input(
    "Quai as linhas que devem ser trocadas na matriz (digite na mesma linha)? ").split())

matriz = trocar(matriz, linhas, colunas)
print_matriz(matriz)
