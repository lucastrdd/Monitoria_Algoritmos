'''
Faça uma função recursiva que exiba o n-ésimo termo da sequência de Fibonacci
'''


def fibonacci(num):
    if (num == 1):
        return 1
    elif (num == 2):
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


numero = int(input("Digite um valor inteiro: "))
print(fibonacci(numero))
