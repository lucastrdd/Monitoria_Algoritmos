def fatorial (num):
    if (num == 1):
        return 1
    else:
        return num * fatorial(num - 1)

num = int(input('Digite um número inteiro: '))
print(fatorial(num))

input()