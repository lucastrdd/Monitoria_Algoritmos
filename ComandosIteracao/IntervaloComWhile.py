# Crie um programa que mostre na tela todos os números pares num intervalo que
# o usuário informar.
# Passos:

# Pedir a informação
num = int(input('Digite um número inteiro:'))
cont = 0
i = 0

# Calcula
while(i <= num):
    if (i % 2 == 0):
        print(i, ' ', end='')
        cont += 1
    i += 1

# Retorna
print()
print(f'Existem {cont} números pares no intervalo de 0 até {num}')