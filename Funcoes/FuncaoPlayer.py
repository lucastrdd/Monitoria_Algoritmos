'''
Crie uma função que manipule a vida de um player diminuindo-a para todo o escopo do programa
seja quando uma função de inimigos inflige danos, ou elementos do cenário que causem danos
também forem executadas.
'''
import random


def dano(hp):
    print()
    chave = random.randrange(1, 3)
    if (chave == 1):
        hp -= 5
        print("Tomou dano do cenário (5)")
        print("A vida do player é de:", hp)
    else:
        hp -= 20
        print("Tomou dano do inimigo (20)")
        if hp != 0:
            print("A vida do player é de:", hp)
    return hp


player = 100
print(f"Player com {player} de hp")
input("Pressione Enter para prosseguir")
while (player >= 20):
    player = dano(player)
    if player > 0:
        input("Pressione Enter para prosseguir")
print()
if player > 0:
    print(f"Tomou dano do inimigo ({player})")
    player -= player

print()
print(f"O player atingiu {player} vida ")
