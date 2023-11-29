'''
Faça um sistema que cadastre filmes usando um dicionario e uma lista, e os imprima depois
'''

lista = []
for i in range(0, 2):
    filmes = {"Título": str(input("Qual o nome do filme? ")), "Ano":
              int(input("Qual o ano do filme? "))}
    lista.append(filmes)

for filme in lista:
    print(f"O nome é {filme['Título']} o ano é {filme['Ano']}")
