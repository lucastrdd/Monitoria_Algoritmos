def inverter (num):
    inv = 0

    while (num != 0):
        resto = num % 10
        inv = inv * 10 + resto
        num = (num - resto) // 10

    return inv


valor = int(input("Digite um número inteiro: "))
print(f"O inverso de '{valor}' é '{inverter(valor)}'")