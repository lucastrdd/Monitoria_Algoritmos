def fatorial(num):
    prod = 1
    for i in range(num, 0, -1):
        prod *= i
    print(prod)


num1 = int(input('Digite um número inteiro: '))
fatorial(num1)
