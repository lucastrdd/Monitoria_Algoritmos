def calcular(num1, num2, cont=2, mdc=1):

    if num1 <= 1 and num2 <= 1:
        print(f"{num1:4d}{num2:4d}|-----")
        return mdc

    elif num1 % cont == 0 and num2 % cont == 0:
        print(f"{num1:4d}{num2:4d}|{cont:2d}")
        num1 //= cont
        num2 //= cont
        mdc *= cont
        return calcular(num1, num2, cont, mdc)

    elif num1 % cont == 0 or num2 % cont == 0:

        if num1 % cont == 0:
            print(f"{num1:4d}{num2:4d}|{cont:2d}")
            num1 //= cont

        else:
            print(f"{num1:4d}{num2:4d}|{cont:2d}")
            num2 //= cont

        return calcular(num1, num2, cont, mdc)

    return calcular(num1, num2, cont + 1, mdc)


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"O fatorial de {a} e {b} é {calcular(a,b)}")
