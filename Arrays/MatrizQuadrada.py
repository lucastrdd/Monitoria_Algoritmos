'''
Dada uma matriz, escreva um código para verificar se ela é quadrada.
'''
from random import randint


def criar(l, c):
    vetor = []
    for i in range(l):
        vetor.append([])
        for j in range(c):
            vetor[i].append(randint(0, 9))
    return vetor


def simetrica(matriz):

    for l in range(len(matriz)):
        c = len(matriz[l])
        if (c != len(matriz)):
            return False

    return True


mat = criar(int(input("Quantas linhas? ")), int(input("Quantas colunas? ")))
if (simetrica(mat)):
    print("É simétrica")
else:
    print("Não é simétrica")
