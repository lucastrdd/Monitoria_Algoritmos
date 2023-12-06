'''
Crie um programa que receba a nota dos alunos de uma turma até o usuário digitar -1, e então mostre
a média da turma e qual a maior nota.s
'''

nota = int(input("Informe a nota (-1 interrompe): "))
contagem = 0
aux = 0
maior = 0

while (nota != -1):
    if (nota > maior):
        maior = nota
    aux += nota
    contagem += 1
    nota = int(input("Informe a nota (-1 interrompe): "))

print(f"A média de notas é: {aux/contagem} \nE a maior nota é: {maior}")
