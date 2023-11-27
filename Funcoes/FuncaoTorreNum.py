'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
Para um n informado pelo usuário.
Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''
def torre (num):
    for i in range(1,(num + 1)):
        print(i, " ", end='')
        for j in range(1,(i)):
            print (i, " ", end='')
        print()

num = int(input("Digite um valor para realizar a impressão: "))
torre(num)